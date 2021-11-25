import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# function to be fed to curve_fit
def func_1(x, a, b, c):
    return a * np.exp(-b * x) + c

# function to be fed to polyfit
def func_2(x, a, b, c):
    return a*x**2 + b*x + c

# Preparing the data
xdata = np.linspace(0, 4, 50)
y = func_1(xdata, 2.5, 1.3, 0.5)
rng = np.random.default_rng()
y_noise = 0.2 * rng.normal(size=xdata.size)
ydata = y + y_noise

# curve_fit approximation
popt, pcov = curve_fit(func_1, xdata, ydata)
print(popt)

# Plot 1
plt.subplot(2, 2, 1)
plt.plot(xdata, ydata, 'b-', label='data')
plt.plot(xdata, func_1(xdata, *popt), 'r-', label='fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(popt))
plt.xlabel('curve_fit')
plt.legend()

# polyfit approximation
coeff = np.polyfit(xdata, ydata, 2)
print(coeff)

# Plot 2
plt.subplot(2, 2, 2)
plt.plot(xdata, ydata, 'b-', label='data')
plt.plot(xdata, func_2(xdata, *coeff), 'r-', label='fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(coeff))
plt.xlabel('np.polyfit (2-nd order polynomial)')
plt.legend()

plt.show()