import numpy as np
import matplotlib.pyplot as plt
from sympy import diff
import math

def func(n):
    return 2*n**2-0.5**n-3


def diff(n):
    return 4*n+np.log(2)/(2**n)


def fi(n):
    return -1*np.log2(2*n*n-3)


def methodNewton(a, b, eps):
    x0 = a  # F"(a)*F(a)>0
    count = 0
    delta = 1
    while delta > eps:
        if func(a)*func(b) >= 0:
            return "Choose another interval"
        x = x0-func(x0)/diff(x0)
        delta = abs(x-x0)
        x0 = x
        count += 1
    return [x, count]


def methodHordandKas(a, b, eps):
    x0 = b
    x01 = a
    count = 0
    delta = 1
    while delta > eps:
        if func(a)*func(b) >= 0:
            return "Choose another interval"
        x = x01-func(x01)/(func(x0)-func(x01))*(x0-x01)
        x1 = x01-func(x01)/diff(x01)
        delta = abs(x-x0)/2
        x0 = x
        x01 = x1
        count += 1
    return [x, count]


def methodSimpleIterations(a, b, eps):
    count = 0
    delta = 1
    x0 = b
    while delta > eps:
        if func(a)*func(b) >= 0:
            return "Choose another interval"
        x = fi(x0)
        delta = abs(x-x0)
        x0 = x
        count += 1
    return [x, count]


x = np.arange(-7, 7, 0.1) #График
plt.rc('grid', linestyle="--", color="deeppink")
plt.grid(True)
plt.plot(x, 2*x*x-np.power(0.5, x)-3, lw=1, color="black")
plt.xlabel("X", color="black")
plt.ylabel("Y", color="black")
plt.suptitle("График для отделения корней", color="black")
plt.show()
eps = 0.000001
a = -7
b = -6
x1, k1 = methodNewton(a, b, eps)
print(x1, k1)
x2, k2 = methodHordandKas(a, b, eps)
print(x2, k2)
x3, k3 = methodSimpleIterations(a, b, eps)
print(x3, k3)