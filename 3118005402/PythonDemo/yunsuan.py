from fractions import Fraction


def formula_change(exp):  # 中缀表达式转换成后缀表达式
    if not exp:
        return []
    symbols_rule = {
        '+': 1,
        '-': 1,
        '×': 2,
        '÷': 2,
    }  # 设置运算符号的优先级
    formula_stack = []  # 存放后缀表达式的栈
    symbols_stack = []  # 存放操作符的栈
    ch = exp.split(' ')
    for item in ch:
        if item in ['+', '-', '×', '÷']:  # 转换过程中遇到运算符
            while len(symbols_stack) >= 0:
                if len(symbols_stack) == 0:
                    symbols_stack.append(item)
                    break
                symbol = symbols_stack.pop()
                if symbol == '(' or symbols_rule[item] > symbols_rule[symbol]:
                    symbols_stack.append(symbol)
                    symbols_stack.append(item)
                    break  # 使读取的运算符按照括号以及优先级规则存入运算符栈中
                else:
                    formula_stack.append(symbol)  # 除括号外的其他运算符， 当其优先级高于除'('以外的栈顶运算符时，直接入栈
        elif item == '(':  # 转换过程中遇到（号直接入操作符栈
            symbols_stack.append(item)
        elif item == ')':
            while len(symbols_stack) > 0:
                symbol = symbols_stack.pop()  # 从操作符栈中取出栈顶操作符确认是否存入后缀表达式栈中，且取出的操作符要从栈中删除
                if symbol == '(':
                    break  # 遇到左括号时，由于存放后缀表达式的栈中不存有括号，所以直接把括号内的运算符加入后缀表达式栈中即可，
                else:
                    formula_stack.append(symbol)  # 将括号内的运算符号存入转换结果的栈
        else:
            formula_stack.append(item)  # 数值直接入转换结果的栈
    while len(symbols_stack) > 0:
        formula_stack.append(symbols_stack.pop())
    return formula_stack


def formula_result(exp):
    formula_value = []
    for item in exp:
        if item in ['+', '-', '×', '÷']:
            y = formula_value.pop()
            x = formula_value.pop()  # 取出运算符的前两个数字用作运算
            result = calculate(x, y, item)
            if result is False or result < 0:  # 排除计算过程中产生负数以及除数为0的异常情况
                return False
            formula_value.append(result)
        else:
            if item.find('/') > 0:
                left = 0
                if item.find("'") > 0:
                    num = item.split("'")
                    left = int(num[0])
                    right = num[1]
                else:
                    right = item
                num = right.split('/')
                result = Fraction(left * int(num[1]) + int(num[0]), int(num[1]))
                formula_value.append(result)
            else:
                formula_value.append(int(item))
    return formula_value[0]


def calculate(x, y, symbol):
    if symbol == '+':
        return x + y
    if symbol == '-':
        return x - y
    if symbol == '×':
        return x * y
    if symbol == '÷':
        if y == 0:
            return False
        return Fraction(x, y)


if __name__ == '__main__':
    exam = "( 9 + 5 ) × 3'5/6"
    exam1 = "2 + 1'3/4 × 3"
    result1 = formula_change(exam)
    result2 = formula_change(exam1)
    print(result1)
    print(result2)
    print(formula_result(result1))
    print(formula_result(result2))
