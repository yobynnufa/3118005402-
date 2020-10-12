import re
from yunsuan import formula_change, formula_result
from fractions import Fraction


def formula_answer(formula_list):
    with open('Answer.txt', 'r+', encoding='utf-8') as file:
        file.truncate()
        file.close()
    for i, formula in enumerate(formula_list):
        formula_str = str(i + 1)
        formula_value = str(formula_result(formula_change(formula))) + '\n'
        if formula_value.find('/') > 0:
            num = formula_value.split('/')
            left = int(num[0])
            right = int(num[1])
            if left < right:
                answer = formula_str + ':' + formula_value
            else:
                first = left // right
                numerator = left % right
                formula_value = str(first) + "'" + str(Fraction(numerator, right)) + '\n'
                answer = formula_str + ':' + formula_value
        else:
            answer = formula_str + ':' + formula_value
        with open('Answer.txt', 'a+', encoding='utf-8') as file:
            file.write(answer)
    file.close()


def check(exercisefile, answerfile):
    right_num = 0
    wrong_num = 0
    right_list = []
    wrong_list = []
    exercise_result = []

    try:
        with open(exercisefile, 'r', encoding='utf-8') as file:
            for line in file:
                formula_str = re.findall(r'\d+: (.*) = \n', line)
                if formula_str:
                    formula = formula_str[0]
                else:
                    continue
                formula_value = str(formula_result(formula_change(formula)))
                exercise_result.append(formula_value)
    except IOError:
        print('请查看输入的路径是否正确')

    try:
        with open(answerfile, 'r', encoding='utf-8') as file:
            for i, line in enumerate(file):
                part = line.split(':')
                answer_str = part[1]
                if answer_str.find('/') > 0:
                    left = 0
                    if answer_str.find("'") > 0:
                        num = answer_str.split("'")
                        left = int(num[0])
                        right = num[1]
                    else:
                        right = answer_str
                    num = right.split('/')
                    result = Fraction(left * int(num[1]) + int(num[0]), int(num[1]))
                else:
                    result = int(answer_str)
                if result >= 0:
                    if result == 0:
                        answer = "0"
                    else:
                        answer = str(result)
                else:
                    continue
                if answer == exercise_result[i]:
                    right_num += 1
                    right_list.append(i + 1)
                else:
                    wrong_num += 1
                    wrong_list.append(i + 1)
        with open('Grade.txt', 'w', encoding='utf-8') as file:
            right_str = 'Right:' + str(right_num) + ' ' + str(right_list) + '\n'
            wrong_str = 'Wrong:' + str(wrong_num) + ' ' + str(wrong_list)
            file.write(right_str)
            file.write(wrong_str)
    except IOError:
        print('请查看输入的路径是否正确')


if __name__ == '__main__':
    exp_file = r'Exercises.txt'
    ans_file = r'Answer.txt'
    check(exp_file, ans_file)
