import sympy as sym
from sympy.parsing.sympy_parser import parse_expr
from sympy.parsing.sympy_parser import standard_transformations, implicit_multiplication_application

transformations = (standard_transformations + (implicit_multiplication_application,))

'''
- Относительная погрешность
- Latex'овский синтаксис
'''

'''Передаем функцию в виде строки'''
#str_func = "sin(x) * cos(y) * tan(z)"
str_func = "x / y"

'''Передаем список констант'''
constants = []

'''создаем выражение из нашей строки'''
func = parse_expr(str_func, transformations=transformations)

'''Создаем список из переменных, найденных в выражении'''
func_variables = list(func.free_symbols)

'''Список переменных в виде строк'''
str_func_variables = []

'''Будущий словарик строка-переменная (заполняется в цикле)'''
str_to_var = {}

for i in range(len(func_variables)):
    '''Создание словарика'''
    str_to_var[str(func_variables[i])]= func_variables[i]
    '''Говорим питону, какие переменные обозначаются такими-то символами (нужно для диффиринциирования)'''
    func_variables[i] = sym.Symbol(str(func_variables[i]))
    '''Пополняем список строчко-переменных'''
    str_func_variables.append(str(func_variables[i]))

'''Создаем список элементов, которые не являются константами'''
str_var_only = [x for x in str_func_variables if x not in constants]


diff_func = ""
'''Создаем строку с итоговые дифференциалом'''
for i in range(len(str_var_only)):
    #Временно значения дифференциалов обозначила как d'значение переменной'
    diff ="(" + str(sym.diff(func, str_to_var[str_var_only[i]])) + "* d" + str_var_only[i] + ")**2"
    diff_func += diff
    if i < len(str_var_only)-1:
        diff_func += " + "

diff_func = "sqrt(" + diff_func + ")"
print("Выражение для подсчета косвенной погрешности заданной величины:")
print(diff_func)
