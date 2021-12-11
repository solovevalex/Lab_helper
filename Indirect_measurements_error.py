import sympy as sym
from sympy.parsing.sympy_parser import parse_expr
from sympy.parsing.sympy_parser import standard_transformations, implicit_multiplication_application

transformations = (standard_transformations + (implicit_multiplication_application,))

'''
Получена формула для косвенной погрешности на основании введенной строки-формулы. Требуется добавить:
1) Относительная погрешность
2) Latex'овский синтаксис
+ 3) Обернуть введенную формулу в функцию
+ 4) Обернуть полученную формулу для косвенной погрешности в функцию
5) Добавить check на ошибки в веденной формуле
'''


'''
+1) Парсим функцию
+2) Находим все "символы"
+3) Получаем список констант
+4) Получаем список переменных
- нужен способ обозначения погрешностей в формуле 5) Находим функцию ошибки в виде строки
+6) Парсим ее
- не получится 7) Модифицируем ее
8) Как-то получаем словарь со всеми-всеми значениями
+9) На его основе получаем значения функции и функции ошибки
'''

'''
func_val считает значение переданной функции.
function -- функция;
values -- словарик значений.
'''

'''Передаем функцию в виде строки'''
#str_func = "sin(x) * cos(y) * tan(z)"
str_func = "x * y"

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


str_diff_func = ""
'''Создаем строку с итоговые дифференциалом'''
for i in range(len(str_var_only)):
    #Временно значения дифференциалов обозначила как d'значение переменной'
    diff ="(" + str(sym.diff(func, str_to_var[str_var_only[i]])) + " * d" + str_var_only[i] + ")**2"
    str_diff_func += diff
    if i < len(str_var_only)-1:
        str_diff_func += " + "

str_error_func = "sqrt(" + str_diff_func + ")"
print("Выражение для подсчета косвенной погрешности заданной величины:")
print(str_error_func)

error_func = parse_expr(str_error_func, transformations=transformations)

#плохо...
print(str(error_func))


def func_val(function, values):
    value = function.subs(values).evalf()
    return value
