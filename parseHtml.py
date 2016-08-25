from html.parser import HTMLParser
from html.entities import name2codepoint
from urllib.request import urlopen

class MyHTMLParser(HTMLParser):
	def __init__(self):
		self.times = []
		self.location=[]
		self.titles=[]
		self.flags=[False,False,False]
		super(MyHTMLParser,self).__init__()
  
	def handle_starttag(self,tag,attrs):
		try:
			if tag=='h3'  and attrs[0][1]=='event-title':
				self.flags[0]=True
			elif 'time'==tag and attrs[0][0]=='datetime':
				#self.times.append(attrs[0][1])
				self.flags[1]=True
			elif 'span'==tag and attrs[0][1]=='event-location':
				self.flags[2]=True
		except IndexError as e:
			pass
	def handle_endtag(self,tag):
		pass
		#print('</%s>'%tag)
	def handle_startendtag(self,tag,attrs):

		pass
		#print('<%s/>'%tag)
	def handle_data(self,data):
		if self.flags[0]:
			self.titles.append(data)
			self.flags[0]=False
		elif self.flags[1]:
			self.times.append(data)
			#print(data)
			self.flags[1]=False
		elif self.flags[2]:
			self.location.append(data)
			
			self.flags[2]=False
		else:
			pass
		#print(data)
	def handle_comment(self,data):
		pass
		#print('<!--',data,'-->')
	def handle_entityref(self,name):
		pass
		#print('&#%s:'% name)
with urlopen('https://www.python.org/events/python-events/') as html:
	parser=MyHTMLParser()
	parser.feed(html.read().decode('utf-8'))
	#print(parser.titles)
	for i in zip(parser.times, parser.titles, parser.location):
		print(i)