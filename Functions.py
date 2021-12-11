import matplotlib
import string
import numpy as np
import random
from scipy.optimize import curve_fit
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import *
from sympy import*
from sympy.parsing.latex import parse_latex
matplotlib.use('TkAgg')

# функция
def func(x_0, *coeffs_0):
    repl = dict(zip(coeffs, coeffs_0))
    repl[x] = x_0
    f = lambdify([x] + coeffs, formula_1)
    return f(x_0, *coeffs_0)

# парсинг формулы и поиск коэффициентов
def parse(formula):
    global coeffs
    global x
    global formula_1
    x = symbols('x')
    formula_1 = parse_latex(formula)
    variables = formula_1.atoms(Symbol)
    coeffs = []
    for v in variables:
        if v != x:
            coeffs.append(v)
    return formula_1, coeffs

# очистка данных от знаков препинания, преобразования их массивы np.arrays
def data_preparing(x, y):
    for i in range(len(x)):
        for p in string.punctuation:
            if p in x[i] and (p != '.'):
                x[i] = x[i].replace(p, '').split()
            if p in y[i] and (p != '.'):
                y[i] = y[i].replace(p, '').split()
        x[i] = np.array(x[i], dtype='float64')
        y[i] = np.array(y[i], dtype='float64')
    return x, y

# поиск коэффициентов МНК
def approximation(x, y, coeffs):
    xdata = []
    ydata = []
    popt = []
    pcov = []
    for i in range(len(x)):
        xdata.append(x[i])
        ydata.append(y[i])
        Popt, Pcov = curve_fit(func, x[i], y[i], p0=np.ones(len(coeffs), dtype=float))
        popt.append(Popt)
        pcov.append(Pcov)
        print(x[i])
        print(y[i])
        print(Popt, Pcov)
    return xdata, ydata, popt, pcov

# поиск нулей функции
def find_roots(xdata, coeffs, a):
    f = func(x, *coeffs)

    def f_deriv(a):
        d1 = f.diff(x, 1)
        d2 = lambdify(x, d1)
        return d2(a)

    def find_root(func, f_deriv, x_0, max_steps=30, delta=0.001):
        x_old = x_0
        for i in range(max_steps):
            try:
                x_new = x_old - func(x_old, *coeffs) / f_deriv(x_old)
            except ZeroDivisionError:
                return None
            if abs(x_new - x_old) < delta:
                break
            x_old = x_new
        return x_new

    roots = []
    for i in range(10):
        min, max = np.min(xdata), np.max(xdata)
        x_0 = min + (max - min)*i/10
        r = find_root(func, f_deriv, x_0)
        if (not r) or (abs(func(r, *coeffs))) > 0.001:
            continue
        if r not in roots:
            roots.append(r)
        a.scatter(r, func(r, *coeffs), c=255)
    return roots

# поиск экстремумов функции
def find_extrems(xdata, coeffs, a):
    f = func(x, *coeffs)

    def f_deriv(a):
        d1 = f.diff(x, 1)
        d2 = lambdify(x, d1)
        return d2(a)

    def f_second_deriv(a):
        d3 = f.diff(x, 2)
        d4 = lambdify(x, d3)
        return d4(a)

    def find_local_min(f_deriv, f_second_deriv, x_0, max_steps=30, delta=0.001):
        x_old = x_0
        for i in range(max_steps):
            try:
                x_new = x_old - f_deriv(x_old) / f_second_deriv(x_old)
            except ZeroDivisionError:
                return None
            if abs(x_new - x_old) < delta:
                break
            x_old = x_new
        return x_new

    extrems = []
    for i in range(10):
        min, max = np.min(xdata), np.max(xdata)
        x_0 = min + (max - min)*i/10
        x_min = find_local_min(f_deriv, f_second_deriv, x_0)
        if (not x_min) or (abs(func(x_min, *coeffs))) > 0.001:
            continue
        if x_min not in extrems:
            extrems.append(x_min)
        a.scatter(x_min, func(x_min, *coeffs))
    return extrems

# рисование графика в окне tkinter
def plotting(formula, xdata, ydata, popt, pcov, title, x_label, y_label, error, roots, extr):
    window = Tk()
    window.title("График зависимости")

    fig = Figure(figsize=(6, 6))
    a = fig.add_subplot(111)

    for i in range(len(xdata)):
        s = 'Аппроксимация МНК:'
        for j in range(len(coeffs)):
            s += str(coeffs[j]) + ' = ' + str(popt[i][j]) + '\n'
        c = np.random.rand(3,)
        a.plot(xdata[i], ydata[i], 'o', color=c)
        xdata_1 = np.linspace(np.min(xdata[i]), np.max(xdata[i]), 100)
        a.plot(xdata_1, func(xdata_1, *popt[i]), '-', color=c)

    formula = "y(x) = " + "$" + formula + "$"
    a.legend(loc='upper left', shadow=True, title=formula)
    a.set_title(title, fontsize=16)
    a.set_xlabel(x_label, fontsize=14)
    a.set_ylabel(y_label, fontsize=14)

    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.get_tk_widget().pack()
    canvas.draw()

    text = Text(width=50, height=10)
    text.pack()

    for i in range(len(xdata)):
        sigma = np.sqrt(np.diag(pcov[i]))
        if error:
            text.insert(1.0, 'sigma_' + str(i+1) + ' = ' + str(sigma) + '\n')
        if roots:
            roots = find_roots(xdata[i], popt[i], a)
            text.insert(2.0, 'roots_' + str(i+1) + '=' + str(roots) + '\n')
        if extr:
            extrems = find_extrems(xdata[i], popt[i], a)
            text.insert(3.0, 'extrems_' + str(i+1) + '=' + str(extrems) + '\n')
    text.insert(1.0, formula)

    window.mainloop()