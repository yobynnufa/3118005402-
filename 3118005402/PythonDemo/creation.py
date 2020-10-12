from random import randint
from fractions import Fraction
from yunsuan import formula_result, formula_change


class configuration:
    def __init__(self, formula_num=10, num_length=10, symbols_num=3):
        self.formula_num = formula_num
        self.num_length = num_length
        self.symbols_num = symbols_num


class construction:
    def construct_symbol(self):  # 随机生成运算符
        symbols = ['+', '-', '×', '÷']
        return symbols[randint(0, len(symbols) - 1)]  # 通过随机的位置号来确认对应的运算符

    def construct_fraction(self, num_length):
        denominator = randint(2, num_length)
        numerator = randint(1, denominator - 1)
        first_num = randint(0, num_length - 1)
        fraction = str(Fraction(numerator, denominator))
        if first_num != 0:
            fraction = str(first_num) + "'" + fraction
        return fraction

    def construct_operand(self, fraction_need, num_length):  # 生成运算数据
        if not fraction_need:
            return self.construct_fraction(num_length)  # 随机生成运算范围内的真分数作为运算数据
        else:
            return str(randint(0, num_length - 1))  # 随机生成运算数范围内的整数作为运算数据

    def construct_formula_parentheses(self, formula, num_number):
        formulas = []
        num = num_number
        if formula:
            formula_length = len(formula)
            left_position = randint(0, int(num / 2))
            right_position = randint(left_position + 1, int(num / 2) + 1)
            position_mark = -1
            for i in range(formula_length):
                if formula[i] in ['+', '-', '×', '÷']:
                    formulas.append(formula[i])  # 运算符直接入栈
                else:
                    position_mark += 1
                    if position_mark == left_position:  # 当位置标记与随机生成的左括号位置一致时，左括号先入栈运算数据后入栈
                        formulas.append('(')
                        formulas.append(formula[i])
                    elif position_mark == right_position:  # 当位置标记与随机生成的右括号位置一致时，操作数先入栈运算数据后入栈
                        formulas.append(formula[i])
                        formulas.append(')')
                    else:
                        formulas.append(formula[i])  # 运算数据直接入栈
        if formulas[0] == '(' and formulas[-1] == ')':  # 若生成的括号表达式形如(x+y+z)则重新生成括号表达式
            formulas = self.construct_formula_parentheses(formula, num_number)
            return formulas
        return formulas

    def construct(self, Configuration):
        formula_num = Configuration.formula_num
        formula_list = []
        i = 0
        while i < formula_num:
            ran_symbols_num = randint(1, Configuration.symbols_num)
            parentheses_need = randint(0, 1)
            num_number = ran_symbols_num + 1
            formula = []
            for j in range(ran_symbols_num + num_number):
                if j % 2 == 0:
                    formula.append(self.construct_operand(randint(0, 3), Configuration.num_length))
                    if j > 1 and formula[j - 1] == '÷' and formula[j] == '0':
                        while True:
                            formula[j - 1] = self.construct_symbol()
                            if formula[j - 1] == '÷':
                                continue
                            else:
                                break
                else:
                    formula.append(self.construct_symbol())

            if parentheses_need and num_number != 2:
                formulas = " ".join(self.construct_formula_parentheses(formula, num_number))
            else:
                formulas = " ".join(formula)
            if formula_result(formula_change(formulas)) is False:
                continue
            else:
                formula_list.append(formulas)
                print('第%d道题' % int(i + 1))
                i = i + 1

        return formula_list

    def formula_output(self, formula_list):
        if not formula_list:
            return
        with open('Exercises.txt', "r+", encoding='utf-8') as file:
            file.truncate()
            file.close()
        for i, formula in enumerate(formula_list):
            formula_str = str(i + 1) + ': ' + formula + ' = ' + "\n"
            with open('Exercises.txt', "a+", encoding='utf-8') as file:
                file.write(formula_str)
        file.close()


if __name__ == '__main__':
    pass
