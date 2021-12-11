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


str_diff_func_user = ""
str_diff_func_calc = ""
diff_list = []
'''Создаем строку с итоговые дифференциалом'''
for i in range(len(str_var_only)):
    #Временно значения дифференциалов обозначила как d'значение переменной'
    diff_user ="(" + str(sym.diff(func, str_to_var[str_var_only[i]])) + " * d" + str_var_only[i] + ")**2"
    diff_list.append("d" + str_var_only[i])
    diff_calc ="(" + str(sym.diff(func, str_to_var[str_var_only[i]])) + str_var_only[i].upper() + ")**2"
    str_diff_func_user += diff_user
    str_diff_func_calc += diff_calc
    if i < len(str_var_only)-1:
        str_diff_func_user += " + "
        str_diff_func_calc += " + "

str_error_func_user = "sqrt(" + str_diff_func_user + ")"
str_error_func_calc = "sqrt(" + str_diff_func_calc + ")"
print("Выражение для подсчета косвенной погрешности заданной величины:")
print(str_error_func_user)

error_func = parse_expr(str_error_func_calc, transformations=transformations)



'''!!! Для Саши'''
'''constants -- список констант (совпадает с тем, что ты передаешь мне в начале)'''
print(constants)
'''str_var_only -- список средних значений переменных'''
print(str_var_only)
'''diff_list = список дифференциалов'''
print(diff_list)

'''
func_val считает значение переданного выражения.
function -- функция;
values -- словарик значений.
'''
def func_val(function, values):
    value = function.subs(values).evalf()
    return value
