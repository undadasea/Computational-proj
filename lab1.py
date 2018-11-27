import matplotlib.pyplot as plt
from sympy import Symbol, exp
import scipy.optimize
import math
import numpy as np

p1 = 1
p4 = 2
p5 = 2
p6 = 0
p7 = 0
p8 = 1000
p9 = 22

x1_array = []
x2_array = []
x3_array = []
x3_array0 = []
x3_array1 = []
x3_array2 = []
x4_array0 = []
x4_array1 = []
x4_array2 = []
x4_array = []
p2_array = []

x4_array_bifurc_real = []
p2_array_bufurc_real = []
x4_array_bifurc_complex = []
p2_array_bufurc_complex = []

x2 = 0.1

def x3(x4):
    return (x1 * p9 - x2 + x4 + p5 * (x4 - p7)) / p9


def F(x4):
    E4 = scipy.exp(x4 / (1 + x4 / p8))
    X3 = x3(x4)
    return x1 - X3 + p2 * (1 - X3) * E4

while(x2 < 7.25):
    x1 = (x2 + p4*(x2 - p6))/p9
    E2 = math.exp(x2/(1 + x2/p8))
    p2 = x1/((1 - x1)*E2)
    p3 = p2

    print('x2 = ', x2)
    print('x1 = ', x1)
    print('p2 = ', p2)

    a = -2.0
    b = 10.0
    upper_limit = b
    x4 = a
    root = []
    step = 0.05
    while x4 <= upper_limit:
        f = F(x4)
        x4 += step
        if f * F(x4) < 0:
            a = x4 - step*3
            b = x4 + step*3
            root.append(scipy.optimize.ridder(F, a, b))

    if len(root) > 0:
        print('roots of F(x4) = ', root)
        for i in range(len(root)):
            print('x3 = ', x3(root[i]))
            x4_array.append(root[i])
            x3_array.append(x3(root[i]))
            p2_array.append(p2)
            if p2 > 0 or x1 > 0 or x3(root[i]) > 0:
                pass
            #     if len(root) == 1:
            #         if root[0] > 4.0:
            #             x1_array.append(x1)
            #             x2_array.append(x2)
            #
            #             x3_array0.append('')
            #             x4_array0.append('')
            #             x3_array1.append('')
            #             x4_array1.append('')
            #             x3_array2.append(x3(root[0]))
            #             x4_array2.append(root[0])
            #             p2_array.append(p2)
            #         else:
            #             x1_array.append(x1)
            #             x2_array.append(x2)
            #
            #             x3_array0.append(x3(root[0]))
            #             x4_array0.append(root[0])
            #             x3_array1.append('')
            #             x4_array1.append('')
            #             x3_array2.append('')
            #             x4_array2.append('')
            #             p2_array.append(p2)
            #     # if len(root) == 2:
            #     #     x3_array0.append(x3(root[0]))
            #     #     x4_array0.append(root[0])
            #     #     x3_array1.append(x3(root[1]))
            #     #     x4_array1.append(root[1])
            #     #     x3_array2.append(x3(root[2]))
            #     #     x4_array2.append('')
            #     if len(root) == 3:
            #         x1_array.append(x1)
            #         x2_array.append(x2)
            #
            #         x3_array0.append(x3(root[0]))
            #         x4_array0.append(root[0])
            #         x3_array1.append(x3(root[1]))
            #         x4_array1.append(root[1])
            #         x3_array2.append(x3(root[2]))
            #         x4_array2.append(root[2])
            #         p2_array.append(p2)

            # else:
            #     sys.exit('out of condition')

    a1 = -1 -p2*E2
    a2 = -(p8**2 * p2 * (x1-1) * E2)/(x2 + p2)**2
    b1 = -p2*p9*E2
    b2 = -1 -(p8**2 * p2 * p9 * (x1-1) * E2)/(x2+p8)**2

    A = [[a1, a2],
         [b1, b2]]
    lambda12 = np.linalg.eig(A)[0]
    if x2 > 0.1 and lambda12.imag == [0.0, 0.0]:
        if lambda12.real[0] * lambda12_prev.real[0] < 0:
            for i in range(len(root)):
                x4_array_bifurc_real.append(root[i])
                p2_array_bifurc_real.append(p2)

    lambda12_prev = lambda12
    print(lambda12)

    for i in range(len(root)):
        E4 = math.exp((root[i] * p8) / (root[i] + p8))
        c3 = -1 - p2 * E4
        c4 = -p2*(x3(root[i]) -1)*p8**2 *E4/(p8+root[i])**2
        d3 = -p2*p9*E4
        d4 = -1 -p2*p9*(x3(root[i]) -1)*p8**2 *E4/(p8+root[i])**2 -p5

        B = [[c3, c4],
             [d3, d4]]
        lambda34 = np.linalg.eig(B)[0]
        print(lambda34.imag)
        if lambda34.imag[0] == 0.0:
            print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

    print('############################################')
    if x2 < 1.6 or (x2 > 2.5 and x2 < 5.8) or x2 > 6.5:
        x2 += 0.01
    else:
        x2 += 0.05

print(x4_array1)

# plt.plot(p2_array, x1_array)
# plt.savefig('plot_x1.png')
# plt.clf()
#
# plt.plot(p2_array, x2_array)
# plt.savefig('plot_x2.png')
# plt.clf()
#
# plt.plot(p2_array, x3_array0)
# plt.savefig('plot_x3_0.png')
# plt.clf()
#
# plt.plot(p2_array, x3_array1)
# plt.savefig('plot_x3_1.png')
# plt.clf()
#
# plt.plot(p2_array, x3_array2)
# plt.savefig('plot_x3_2.png')
# plt.clf()
#
# plt.plot(p2_array, x4_array0)
# plt.savefig('plot_x4_0.png')
# plt.clf()
#
# plt.plot(p2_array, x4_array1)
# plt.savefig('plot_x4_1.png')
# plt.clf()
#
# plt.plot(p2_array, x4_array2)
# plt.savefig('plot_x4_2.png')
# plt.clf()
#######################################################
# plt.clf()
# plt.plot(p2_array, x3_array, 'r,')
# plt.savefig('plot_x3_additional.png')
# plt.clf()

# plt.plot(p2_array, x4_array, 'g,')
# plt.savefig('plot_x4_additional.png')
# plt.clf()

