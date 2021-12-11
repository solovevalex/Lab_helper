import matplotlib
matplotlib.use('TkAgg')
from Functions import*

def plotting_graph(formula: str, x: list, y: list, title: str,
                   x_label: str, y_label: str, error: bool, roots: bool, extr: bool):
    '''
    Рисует график функции.
    :param formula: формула y(x) = ...
    :param x: список значений x для N графиков [[x1, x2], [x1', x2'], ...]
    :param y: список значений y для N графиков [[y1, y2], [y1', y2'], ...]
    :param title: заголовок графика
    :param x_label: заголовок оси х графика
    :param y_label: заголовок оси y графика
    :param error: нужны ли погрешности
    :param roots: нужны ли нули функции
    :param extr: нужны ли экстремумы функции
    :return: check: bool (check == True, если график можно построить, иначе check == False)
    '''

    formula_1, coeffs = parse(formula)
    x, y = data_preparing(x, y)
    xdata, ydata, popt, pcov = approximation(x, y, coeffs)
    plotting(formula, xdata, ydata, popt, pcov, title, x_label, y_label, error, roots, extr)

    return

# пример входных данных
formula = r"a \cdot x^3 + b \cdot x^2"
formula = "a*x+b"
# x = [[-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5], [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]]
# y = [[0, 16, 18, 12, 4, 0, 6, 28, 72, 144, 250], [0, 32, 36, 24, 8, 0, 12, 56, 144, 288, 500]]
x = [[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]]
y = [[3.216, 6.424, 9.658, 12.881, 16.081],[4.123, 8.257, 12.381,16.503, 20.629],[4.243, 8.469, 12.721, 16.964, 21.195]]
title = 'резонансные частоты гармоник'
x_label = 'n'
y_label = 'f, кГц'
error = False
roots = False
extr = False
plotting_graph(formula, x, y, title, x_label, y_label, error, roots, extr)

