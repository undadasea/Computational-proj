from method_def import k, q, function, u, TMA, nu1, nu2, test
import numpy as np

# a1 = [0.0, -1.0, -1.0, -1.0, 0.0] #lower diagonal
# b1 = [0.0, -1.0, -1.0, -1.0, 0.0]  #upper diagonal
# c1 = [1.0, 2.5, 2.5, 2.5, 1.0]  #central
# n1 = 5
# f1 = [1.0, 0.5, 0.5, 0.5, 1.0]
# v1 = [4, 5, 4, 5, 4] #test vector
# x1 = np.empty(5)
#print('v = ', metha1, b1, c1, n1, f1, x1))

print(function(0.4))


N = 5
# the length of a brick
left = 0
right = 2

print('N = ', N, ", left, right = ", left, right)

a = np.empty(N+1, dtype='double')
b = np.empty(N+1, dtype='double')
c = np.empty(N+1, dtype='double')
g = np.empty(N+1, dtype='double')
# nu = np.ones(N+1)


h = (right-left)/N
print('h = ', h)

#сетка
x_1 = np.empty(N+1, dtype='double')
for i in range(N+1):
	x_1[i] = (left + i*h)

#сетка половинок
x_12 = np.empty(N+1-1, dtype='double')
for i in range(N+1-1):
	x_12[i] = (x_1[i]+x_1[i+1])/2

#половинный шаг
h_12 = h/2
print('h12 = ', h_12)

# array u
u_ = np.zeros(N+1, dtype='double')
for i in range(N+1):
	u_[i] = u(x_1[i])



for i in range(N+1):
	if i == 0:
		a[i]=0.0
		c[i]=1.0
		b[i]=0.0
		# b[i] = -k_func(x_12[i])/h
		g[i] = u(left)
		# f[i] = h_12*function(x_1[i])
	if i == N+1-1:
		a[i]=0.0
		c[i]=1.0
		b[i]=0.0
		g[i]=u(right)
	if (i != 0) & (i != N+1-1):
		b[i]= -k(x_12[i])/h
		c[i]= (k(x_12[i])/h + k(x_12[i-1])/h + h_12*q(x_1[i]))
		a[i]= -k(x_12[i-1])/h
		g[i]= h_12*function(x_1[i])

# what's the diff between h_12 and x_12?
# why does h increas? (if it's an array)
# h was left the same, use only for a homogeneous net

print("x_1[]", x_1)
print("x_12[]", x_12, '\n')
print("a[]", a)
print("b[]", b)
print("c[]", c)
print("g[]", g)


v = np.empty(N+1, dtype='double')
TMA(a.copy(), c.copy(), b.copy(), g.copy(), v)
print('v = ', v)
print('u_ = ', u_)

# g_ for checking
g_ = np.zeros(N+1, dtype='double')

for i in range(N):
	g_[i] = a[i]*u_[i-1] + c[i]*u_[i] + b[i]*u_[i+1]

g_[N] = c[N]*nu1(u(right))
print('g_ = ', g_)

diff = np.empty(N+1, dtype='double')
for i in range(N+1):
	# print("v - u: ", '%e' % (v[i] - u(x_1[i])))
	diff[i] = np.fabs(v[i] - u(x_1[i]))

print(diff)
print('max E = ', np.sort(diff)[N])


