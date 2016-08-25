def foo(s):
	n=int(s)
	if n==0:
		raise ValueError('invalid value:%s'% s)
	return 1/n

def bar():
	try:
		foo('0')
	except ValueError as e:
		print('ValueError!')
		raise #记录一下方便后续追踪，并且同时raise不带参数，就会把当前错误原样输出


bar()