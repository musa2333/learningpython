#import logging

#def foo(s):
#	return 10/int(s)

#def bar(s):
#	return foo(s)*2

#def main():
#	try:
#	    bar('0')
#	except Exception as e:
#		logging.exception(e)

#main()
#print('END')
class FooEroor(ValueError) :
	pass

def foo(s):
	n=int(s)
	if n==0:
		raise FooEroor('invalid value:%s'% s)
	return 1/n
foo('0')