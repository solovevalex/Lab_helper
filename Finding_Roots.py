import matplotlib.pyplot as plt
import numpy as np
import random

# function to find the roots of
def f(x):
    return x**3 - 5*x**2

# derivative of the function
def f_deriv(x):
    return 3*x**2 - 10*x

# drawing the plot
def draw_f():
    x = np.linspace(-10, 10, 100)
    plt.plot(x, f(x))
    plt.title('$x**4 + x**3 - 5*x**2 - 10$ - Newtons Method')

# function finding roots via Newton's Method
def find_root(f, f_deriv, x_0, max_steps = 30, delta = 0.001):
    x_old = x_0
    for i in range(max_steps):
        try:
            x_new = x_old - f(x_old)/f_deriv(x_old)
        except ZeroDivisionError:
            return None

        if abs(x_new - x_old) < delta:
            break

        x_old = x_new

    return x_new

draw_f()

for i in range(10):
    x_0 = random.randint(-10, 10)
    r = find_root(f, f_deriv, x_0)
    if (not r) or (abs(f(r))) > 0.001:
        continue
    plt.scatter(r, f(r))

plt.show()