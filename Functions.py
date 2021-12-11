import matplotlib
import numpy as np
from scipy.optimize import curve_fit
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import *
from sympy import*
from sympy.parsing.latex import parse_latex
matplotlib.use('TkAgg')


def check_types(formulas, x, y, error, roots, extr):
    check_1 = True
    if type(error) is not bool or type(roots) is not bool or type(extr) is not bool:
        check_1 = False
    if type(formulas) is list:
        for f in formulas:
            if type(f) is not str:
                check_1 = False
    else:
        check_1 = False
    if type(x) is list and type(y) is list:
        for i in range(len(x)):
            if type(x[i]) is not str or type(y[i]) is not str:
                check_1 = False
        if len(x) != len(y):
            check_1 = False
    else:
        check_1 = False
    return check_1

# функция

def factory(i):
    def f(x_0, *coeffs_0):
        f = lambdify([x] + coeffs_1[i], formulas_1[i])
        return f(x_0, *coeffs_0)
    return f

def generate_functions(N):
    functions = []
    for i in range(N):
        functions.append(factory(i))
    return functions

# парсинг формулы и поиск коэффициентов
def parse(formulas):
    global coeffs_1
    global x
    global formulas_1
    x = symbols('x')
    formulas_1 = []
    coeffs_1 = []
    for f in formulas:
        f_1 = parse_latex(f)
        formulas_1.append(f_1)
        variables_1 = f_1.atoms(Symbol)
        coeffs = []
        for v in variables_1:
            if v != x:
                coeffs.append(v)
        coeffs_1.append(coeffs)
    print(formulas_1, coeffs_1)
    return formulas_1, coeffs_1

# очистка данных от знаков препинания, преобразования их массивы np.arrays
def data_preparing(x, y):
    for i in range(len(x)):
        x[i] = x[i].replace(',', '.').split()
        y[i] = y[i].replace(',', '.').split()
        x[i] = np.array(x[i], dtype='float64')
        y[i] = np.array(y[i], dtype='float64')
    return x, y

def rounding(popt, sigma):
    for i in range(len(popt)):
        for j in range(len(sigma[i])):
            n = sigma[i][j]
            s = '%1.5e' % n
            if 'e-' in s:
                s = s.split('e-')
                sigma[i][j] = str(round(float(s[0]), 1)) + 'e-' + str(s[1])
                popt[i][j] = '%1.5e' % round(popt[i][j], int(s[-1]))
            elif 'e+' in s:
                s = s.split('e+')
                sigma[i][j] = str(round(float(s[0]), 1)) + 'e+' + str(s[1])
                popt[i][j] = '%1.5e' % round(popt[i][j], -int(s[-1]))
    return popt, sigma

# поиск коэффициентов МНК
def approximation(xdata, ydata, coeffs_1):
    check_2 = True
    popt = []
    pcov = []
    functions = generate_functions(len(xdata))
    for i in range(len(xdata)):
        try:
            Popt, Pcov = curve_fit(functions[i], xdata[i], ydata[i], p0=np.ones(len(coeffs_1[i]), dtype=float))
        except ValueError or RuntimeError:
            check_2 = False
        else:
            popt.append(Popt)
            pcov.append(Pcov)
    print(popt, pcov)
    return popt, pcov, check_2

# поиск нулей функции
def find_roots(func, xdata, coeffs, a):
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
        r = round(r, 5)
        if r not in roots:
            roots.append(r)
        a.scatter(r, func(r, *coeffs), c=255)
    return roots

# поиск экстремумов функции
def find_extrems(func, xdata, coeffs, a):
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
        x_min = round(x_min, 5)
        if x_min not in extrems:
            extrems.append(x_min)
        a.scatter(x_min, func(x_min, *coeffs))
    return extrems

# рисование графика в окне tkinter
def plotting(formulas, xdata, ydata, popt, pcov, title, x_label, y_label, error, roots, extr):
    window = Tk()
    window.title("График зависимости")

    fig = Figure(figsize=(6, 6))
    a = fig.add_subplot(111)
    functions = generate_functions(len(xdata))

    sigma = []
    for i in range(len(pcov)):
        sigma.append(np.sqrt(np.diag(pcov[i])))
    popt, sigma = rounding(popt, sigma)

    for i in range(len(xdata)):
        formula = "y(x) = " + "$" + formulas[i] + "$"
        s = str(i+1) + ') ' + str(formula) + ", "
        for j in range(len(coeffs_1)):
            s += str(coeffs_1[i][j]) + ' = ' + str(popt[i][j]) + '\n'
        c = np.random.rand(3,)
        a.plot(xdata[i], ydata[i], 'o', color=c)
        xdata_1 = np.linspace(np.min(xdata[i]), np.max(xdata[i]), 100)
        a.plot(xdata_1, functions[i](xdata_1, *popt[i]), '-', color=c, label=s)

    a.legend(loc=0, shadow=True)

    a.set_title(str(title), fontsize=16)
    a.set_xlabel(str(x_label), fontsize=14)
    a.set_ylabel(str(y_label), fontsize=14)

    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.get_tk_widget().pack(side="top",fill='both',expand=True)
    canvas.draw()

    text = Text(width=50, height=10)
    text.pack()

    for i in range(len(xdata) - 1, -1, -1):
        if error:
            text.insert(1.0, 'sigma_' + str(i + 1) + ' = ' + str(sigma[i]) + '\n')
        if roots:
            roots = find_roots(functions[i], xdata[i], popt[i], a)
            text.insert(2.0, 'roots_' + str(i + 1) + '=' + str(roots) + '\n')
        if extr:
            extrems = find_extrems(functions[i], xdata[i], popt[i], a)
            text.insert(3.0, 'extrems_' + str(i + 1) + '=' + str(extrems) + '\n')
        text.insert(1.0, formulas[i] + '\n')

    window.mainloop()