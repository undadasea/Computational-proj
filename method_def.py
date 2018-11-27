import scipy.misc as sci

# наш точный результат
def u(x):
	#return 1
	return x + 2

def function(x):
	#return 1
	return x*(x + 2)

#половинное должно быть
def k(x):
	#return 1
	return 2

def q(x):
	#return 1
	return x

def nu1(u):
	#return 1
	return u

def nu2(u):
	#return 1
	return u


def TMA(a, c, b, g, x):

	n = len(a) - 1
	# worked with (i+1) was just "i". for granich usl are const
	for i in range(n):
		m = a[i] / c[i-1]
		c[i] = c[i] - m * b[i-1]
		g[i] = g[i] - m * g[i-1]
		print('i = ', i)
		print('c[i] = ', c[i])
		print('g[i] = ', g[i])
	x[n] = (g[n]/c[n])
	print('n = ', n)

	# str_my = 'x[i-1] = (g[i-1] - b[i-1] * x[i] / c[i-1])'
	# str_notmy = 'x[i - 1] = (g[i - 1] - b[i - 1] * x[i]) / c[i - 1]'
	#
	# for i in range(len(str_notmy)):
	# 	print(str_notmy[i], ' = ', ord(str_notmy[i]))

	for i in range(len(g) - 1, -1, -1):
		#print('before. x[', i-1, '] = ', x[i-1])
		# x[i - 1] = (g[i - 1] - b[i - 1] * x[i]) / c[i - 1]
		x[i-1] = (g[i-1] - b[i-1] * x[i]) / c[i-1]
		# print('x[', i-1, '] = ', x[i-1])
		# print('x[', i, '] = ', x[i])
		# print('g[', i - 1, '] = ', g[i - 1])
		# print('b[', i-1, '] = ', b[i-1])
		# print('c[', i-1, '] = ', c[i-1])
		# print('##########################################')
		###########################################################
		# print('before. x[', i, '] = ', x[i])
		# # x[i] = (g[i] - b[i]*x[i+1]/c[i])
		# x[i+1 - 1] = (g[i+1 - 1] - b[i+1 - 1] * x[i+1]) / c[i+1 - 1]
		# print('x[', i, '] = ', x[i])
		# print('x[', i+1, '] = ', x[i + 1])
		# print('g[', i, '] = ', g[i])
		# print('b[', i, '] = ', b[i])
		# print('c[', i, '] = ', c[i])
		# print('##########################################')
	return x

def test(a, b, c):
	a = b[1]+c
	b[1] = 10
	return c
