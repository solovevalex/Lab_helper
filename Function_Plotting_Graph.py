import matplotlib
from Functions import check_types, parse, data_preparing, approximation, plotting
matplotlib.use('TkAgg')

def plotting_graph(formulas: list, x: list, y: list, title: str,
                   x_label: str, y_label: str, error: bool, roots: bool, extr: bool):
    '''
    Рисует график функции.
    :param formulas: формулы y(x) = ... ['formula_1', 'formula_2', ...]
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
    try:
        check_1 = check_types(formulas, x, y, error, roots, extr)
        formulas_1, coeffs_1 = parse(formulas)
        xdata, ydata, check_3 = data_preparing(x, y)
        popt, pcov, check_2 = approximation(xdata, ydata, coeffs_1)
        if check_1 and check_2 and check_3:
            plotting(formulas, xdata, ydata, popt, pcov, title, x_label, y_label, error, roots, extr)
            return True
        else:
            return False
    except BaseException:
        return False

# пример входных данных
# formulas = ['a \cdot x^3 + b \cdot x^2', 'a*x**2 + b']
# x = ['-5 -4 -3 -2 -1 0 1 2 3 4 5', '-5 -4 -3 -2 -1 0 1 2 3 4 5']
# y = ['0 16 18 12 4 0.3 6 28 72 144 250', '375 240 135 60,1 15 0 15 60 135 240 375']
# title = 'График_1'
# x_label = 't, c'
# y_label = 'l, m'
# error = True
# roots = True
# extr = True
# check = plotting_graph(formulas, x, y, title, x_label, y_label, error, roots, extr)