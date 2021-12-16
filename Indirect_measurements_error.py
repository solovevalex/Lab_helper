import sympy as sym
from sympy.parsing.sympy_parser import parse_expr
from sympy.parsing.sympy_parser import standard_transformations, implicit_multiplication_application
'''
+ Добавить check на ошибки в веденной формуле
'''


transformations = (standard_transformations + (implicit_multiplication_application,))

'''exp_value -- считает значение функции, полученной в виде строки.
Передаются значения:
    str_exp -- введенное выражение;
    values -- словарь значений.
Возвращаются:
    value -- значение выражения при введенных переменных.
'''
def exp_value(str_exp, values):
    exp = parse_expr(str_exp, transformations=transformations)
    exp_variables = list(exp.free_symbols)
    values_ = {}
    for i in range(len(exp_variables)):
        exp_variables[i] = sym.Symbol(str(exp_variables[i]))
        values_[exp_variables[i]] = values[str(exp_variables[i])]
    value = exp.evalf(subs=values_)
    return value


'''
get_error_func -- на основе выражения-строки и списка констант считает формулу для косвенной погрешности измерения.
Передаются значения:
    str_exp -- введенное выражение;
    constants -- список констант.
Возвращаются:
    str_error_func_user -- формула косвенной погрешности, для пользователя;
    str_var_only -- список из переменных (их средние значения);
    diff_list_user -- список дифференциалов, для пользователя;
    str_error_func_calc -- формула косвенной погрешности, для рассчетов;
    diff_list_calc -- список дифференциалов, для рассчетов.
'''
def get_error_func(str_exp, constants):
    exp = parse_expr(str_exp, transformations=transformations)
    exp_variables = list(exp.free_symbols)
    str_exp_variables = []
    str_to_var = {}
    for i in range(len(exp_variables)):
        str_to_var[str(exp_variables[i])] = exp_variables[i]
        exp_variables[i] = sym.Symbol(str(exp_variables[i]))
        str_exp_variables.append(str(exp_variables[i]))
    str_var_only = [x for x in str_exp_variables if x not in constants]
    str_diff_func_user = ""
    str_diff_func_calc = ""
    diff_list_user = []
    diff_list_calc = []
    for i in range(len(str_var_only)):
        expr = sym.diff(exp, str_to_var[str_var_only[i]])
        expr = sym.simplify(expr / exp)
        diff_user = "(" + str(expr) + " * d" + str_var_only[i] + ")**2"
        diff_list_user.append("d" + str_var_only[i])
        if str_var_only[i].isupper() == True:
            diff_calc = "(" + str(expr) + " * " + str_var_only[i].lower() + ")**2"
            diff_list_calc.append(str_var_only[i].lower())
        else:
            diff_calc = "(" + str(expr)+ " * " + str_var_only[i].upper() + ")**2"
            diff_list_calc.append(str_var_only[i].upper())
        str_diff_func_user += diff_user
        str_diff_func_calc += diff_calc
        if i < len(str_var_only) - 1:
            str_diff_func_user += " + "
            str_diff_func_calc += " + "
    str_error_func_user = "sqrt(" + str_diff_func_user + ")"
    str_error_func_calc = "sqrt(" + str_diff_func_calc + ")"
    return str_error_func_user, str_var_only, diff_list_user, str_error_func_calc, diff_list_calc

'''
get_f -- делит уравнение на левую и правую часть.
Передаются значения:
    str -- уравнение.
Возвращаются:
    f -- левая часть;
    str_ -- правая часть (выражение для дальнейших подсчетов).
'''
def get_f(str):
    for i in range(len(str)):
        if str[i] == '=':
            f = str[:i]
            str_ = str.replace(f, "").replace('=','')
            break
    f = f.replace(" ", "")
    return f, str_


'''
(функция не расчитана на применение в других файлах!)
get_relative_err -- левая часть выражения.
Передаются значения:
    y -- величина, для которой считаем погрешность;
Возвращаются:
    rel_err -- левая часть.
'''
def get_relative_err(y):
    rel_err = "1/" + y + " * d" + y
    return rel_err

'''
get_final_err_expr -- итоговое выражение для косвенной погрешности.
Передаются значения:
    y -- величина, для которой считаем погрешность;
    err_expr -- правая часть выражения;
Возвращаются:
    final_err_expr -- итоговое выражение для косвенной погрешности.
'''
def get_final_err_expr(y, err_expr):
    rel_err = get_relative_err(y)
    final_err_expr = rel_err + " = " + err_expr
    return final_err_expr

