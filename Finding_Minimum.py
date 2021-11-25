import matplotlib.pyplot as plt
import numpy as np
import random
import sympy as sym
from sympy import*

x = sym.Symbol('x')

# the function to find the minimum of
F = x**3 - 5*x**2

# the function to find the minimum of (the same)
def f(x):
    return x**3 - 5*x**2

# first derivative of the function
def f_deriv(a):
    d1 = F.diff(x, 1)
    d2 = lambdify(x, d1)
    return d2(a)

# second derivative of the function
def f_second_deriv(a):
    d3 = F.diff(x, 2)
    d4 = lambdify(x, d3)
    return d4(a)

# drawing the plot
def draw_f():
    x = np.linspace(-10, 10, 100)
    plt.plot(x, f(x))
    plt.title('$x**4 + x**3 - 5*x**2 - 10$ - Finding Minimum')

# finding the local minimum around the point x_0
def find_local_min(f_deriv, f_second_deriv, x_0, max_steps = 30, delta = 0.001):
    x_old = x_0
    for i in range(max_steps):
        try:
            x_new = x_old - f_deriv(x_old)/f_second_deriv(x_old)
        except ZeroDivisionError:
            return None
        if abs(x_new - x_old) < delta:
            break

        x_old = x_new

    return x_new

draw_f()

# picking up 10 random points to find local minimum around
for i in range(10):
    x_0 = random.randint(-10, 10)
    x_min = find_local_min(f_deriv, f_second_deriv, x_0)
    if (not x_min) or (abs(f(x_min))) > 0.001:
        continue
    plt.scatter(x_min, f(x_min))

plt.show()
