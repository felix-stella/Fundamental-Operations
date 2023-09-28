import random
import math
from unittest import result


class Number:
    def __init__(self, max: int = None, nums: tuple = None):
        if nums:
            if isinstance(nums, tuple) and len(nums) == 3:
                if nums[2] == 0:
                    raise ValueError("分母不能为零。")
                else:
                    self.integer = int(nums[0])
                    self.numerator = int(nums[1])
                    self.denominator = int(nums[2])
            else:
                raise ValueError("nums必须是一个三元组（整数，分子，分母）。")
        else:
            if (not isinstance(max, int)) or max < 1:
                raise ValueError("max必须大于等于1。")
            self.integer = random.randint(0, max)
            self.denominator = random.randint(1, max)
            is_fra = random.randint(1, 2)
            if is_fra == 1:
                self.numerator = random.randint(1, self.denominator)
            else:
                self.numerator = 0

    def reduce_fraction(self):
        '''计算最大公约数（GCD）。'''

        gcd = math.gcd(self.numerator, self.denominator)
        numerator = self.numerator / gcd
        denominator = self.denominator / gcd
        integer = numerator // denominator + self.integer
        numerator = numerator % denominator
        self.integer = int(integer)
        self.numerator = int(numerator)
        self.denominator = int(denominator)

    def __str__(self):
        if self.integer == 0:
            if self.numerator:
                return str(self.numerator) + '/' + str(self.denominator)
            else:
                return '0'
        else:
            if self.numerator:
                return str(self.integer) + '\'' + str(self.numerator) + '/' + str(self.denominator)
            else:
                return str(self.integer)

    def __float__(self):
        return self.integer + self.numerator / self.denominator


class Fraction:
    '''对分数执行算术运算。

    这个类允许你对分数执行加法、减法、乘法和除法运算，并获得简化的结果。

    属性:
        f1 (Number): 运算的第一个分数。
        f2 (Number): 运算的第二个分数（用于二元运算）。
        op (str): 运算的操作符。必须是其中之一：' + ', ' - ', ' * ', 或 ' % '。

    参数:
        f1 (Number): 表示第一个分数的Number类实例。
        f2 (Number): 表示第二个分数的Number类实例。
        op (str): 运算的操作符。必须是其中之一：' + ', ' - ', ' * ', 或 ' % '。

    引发:
        ValueError: 如果提供的参数不是Number类型，或者操作符不是二元运算的' + ', ' - ', ' * ', 或 ' % '之一。

    方法:
        calculate_fractions(): 对分数执行指定的二元运算，并返回简化的结果。

    示例用法:
        # 创建两个分数
        fraction1 = Fraction(Number(nums=(1, 2, 3)), Number(nums=(2, 3, 4)), ' + ')

        # 执行加法运算
        result = fraction1.calculate_fractions()
    '''

    def __init__(self, f1: Number, f2: Number, op: str):
        if isinstance(f1, Number) and isinstance(f2, Number):
            self.f1 = f1
            self.f2 = f2
        else:
            raise ValueError("参数必须是Number类型。")
        if op in [' + ', ' - ', ' * ', ' % ']:
            self.op = op
        else:
            raise ValueError("操作符必须是' + ', ' - ', ' * ', 或 ' % '之一。")

    def calculate_fractions(self):
        if self.op == ' + ':
            denominator = self.f1.denominator * self.f2.denominator
            numerator = (self.f1.integer * self.f1.denominator + self.f1.numerator) * self.f2.denominator \
                        + (self.f2.integer * self.f2.denominator + self.f2.numerator) * self.f1.denominator
            # 创建一个分数作为结果。
            result = Number(nums=(0, numerator, denominator))
        elif self.op == ' - ':
            denominator = self.f1.denominator * self.f2.denominator
            numerator = (self.f1.integer * self.f1.denominator + self.f1.numerator) * self.f2.denominator \
                        - (self.f2.integer * self.f2.denominator + self.f2.numerator) * self.f1.denominator
            result = Number(nums=(0, numerator, denominator))
        elif self.op == ' * ':
            denominator = self.f1.denominator * self.f2.denominator
            numerator = (self.f1.numerator + self.f1.integer * self.f1.denominator) \
                        * (self.f2.numerator + self.f2.integer * self.f2.denominator)
            result = Number(nums=(0, numerator, denominator))
        elif self.op == ' % ':
            # 除法：检查除数（self.f2）是否为零。
            if float(self.f2) == 0:
                raise ValueError("除数不能为零。")
            denominator = self.f1.denominator * (self.f2.numerator + self.f2.integer * self.f2.denominator)
            numerator = (self.f1.numerator + self.f1.integer * self.f1.denominator) * self.f2.denominator
            result = Number(nums=(0, numerator, denominator))

        result.reduce_fraction()
        return result


class Expression:
    def __init__(self, max, question_num):
        self.max = max
        self.question_num = question_num
        self.expressions = set()
        self.expression_lists = []
        self.generation_times = 0
        self.answers = []
        self.questions = []
        self.expression_num = 0

    def generate_subexpression(self, etype, op):
        # 对于etype为1，生成两个在指定最大值（self.max）内的随机分数（num_1和num_2）。
        if etype == 1:
            num_1 = Number(self.max)
            num_1.reduce_fraction()
            num_2 = Number(self.max)
            num_2.reduce_fraction()
            # 如果操作符不是' % '，生成两个Number对象，并将较大的放在前面。
            if op != ' % ':
                if float(num_1) >= float(num_2):
                    subexpression = [num_1, op, num_2]
                else:
                    subexpression = [num_2, op, num_1]
            else:
                subexpression = [num_1, op, num_2]
        else:
            if op in [' - ', ' % ']:
                if random.randint(0, 1):
                    num = Number(self.max)
                    num.reduce_fraction()
                    subexpression = [op, num]
                else:
                    num = Number(self.max)
                    num.reduce_fraction()
                    subexpression = [num, op]
            # 对于其他操作符，生成包含操作符和随机数字的子表达式。
            else:
                num = Number(self.max)
                num.reduce_fraction()
                subexpression = [op, num]
        return subexpression

    def generate_expression_list(self):
        expression_list = []
        sub_num = random.randint(1, 3)  # 生成随机数量的子表达式（1到3个）。
        # 随机选择子表达式的操作符。
        operators = [random.choice([' + ', ' - ', ' * ', ' % ']) for _ in range(sub_num)]
        subexpression_1 = self.generate_subexpression(1, operators[0])
        str_sub_1 = str(subexpression_1[0]) + subexpression_1[1] + str(subexpression_1[2])
        if sub_num == 1:
            expression_list.append(subexpression_1)
            str_sub_2 = ''
            str_sub_3 = ''
            string = str_sub_1 + '|' + str_sub_2 + '|' + str_sub_3
        elif sub_num == 2:
            subexpression_2 = self.generate_subexpression(2, operators[1])
            str_sub_2 = str(subexpression_2[0]) + str(subexpression_2[1])
            str_sub_3 = ''
            expression_list.append(subexpression_1)
            expression_list.append(subexpression_2)
            string = str_sub_1 + '|' + str_sub_2 + '|' + str_sub_3
        # 如果有三个子表达式，确定它们的类型并生成它们。
        else:
            etype = random.randint(1, 2)
            subexpression_2 = self.generate_subexpression(etype, operators[1])
            if etype == 1:
                subexpression_3 = [operators[2]]
                str_sub_2 = str(subexpression_2[0]) + str(subexpression_2[1]) + str(subexpression_2[2])
                str_sub_3 = subexpression_3[0]
                # 比较字符串表示以决定子表达式的顺序。
                if str_sub_1 >= str_sub_2 and operators[2] in [' + ', ' * ']:
                    expression_list.append(subexpression_1)
                    expression_list.append(subexpression_2)
                    expression_list.append(subexpression_3)
                    string = str_sub_1 + '|' + str_sub_2 + '|' + str_sub_3
                else:
                    expression_list.append(subexpression_2)
                    expression_list.append(subexpression_1)
                    expression_list.append(subexpression_3)
                    string = str_sub_1 + '|' + str_sub_2 + '|' + str_sub_3
            else:
                subexpression_3 = self.generate_subexpression(2, operators[2])
                str_sub_2 = str(subexpression_2[0]) + str(subexpression_2[1])
                str_sub_3 = str(subexpression_3[0]) + str(subexpression_3[1])
                expression_list.append(subexpression_1)
                expression_list.append(subexpression_2)
                expression_list.append(subexpression_3)
                string = str_sub_1 + '|' + str_sub_2 + '|' + str_sub_3
        return expression_list, string

    def calculate_answer(self, expression_list):
        expression_1 = Fraction(expression_list[0][0], expression_list[0][2], expression_list[0][1])
        result_1 = expression_1.calculate_fractions()
        # 检查第一个子表达式的结果是否小于零，如果是，则引发异常。
        if float(result_1) < 0:
            raise ValueError("子表达式不能小于零。")
        if len(expression_list) == 1:
            result = result_1
        elif len(expression_list) == 2:
            if isinstance(expression_list[1][0], str):
                expression_2 = Fraction(result_1, expression_list[1][1], expression_list[1][0])
            else:
                expression_2 = Fraction(expression_list[1][0], result_1, expression_list[1][1])
            result = expression_2.calculate_fractions()
        else:
            if len(expression_list[2]) == 1:
                expression_2 = Fraction(expression_list[1][0], expression_list[1][2], expression_list[1][1])
                result_2 = expression_2.calculate_fractions()
                if float(result_2) < 0:
                    raise ValueError("子表达式不能小于零。")
                expression_3 = Fraction(result_1, result_2, expression_list[2][0])
                result = expression_3.calculate_fractions()
            else:
                if isinstance(expression_list[1][0], str):
                    expression_2 = Fraction(result_1, expression_list[1][1], expression_list[1][0])
                else:
                    expression_2 = Fraction(expression_list[1][0], result_1, expression_list[1][1])
                result_2 = expression_2.calculate_fractions()
                if float(result_2) < 0:
                    raise ValueError("子表达式不能小于零。")
                if isinstance(expression_list[2][0], str):
                    expression_2 = Fraction(result_2, expression_list[2][1], expression_list[2][0])
                else:
                    expression_2 = Fraction(expression_list[2][0], result_2, expression_list[2][1])
                result = expression_2.calculate_fractions()
        if float(result) < 0:
            raise ValueError("子表达式不能小于零。")
        return result

    def generate_expressions(self):
        while (self.expression_num < self.question_num):
            self.generation_times += 1
            try:
                exp_list, exp_string = self.generate_expression_list()
                answer = self.calculate_answer(exp_list)
            # 如果在表达式生成或计算过程中发生异常（例如，除以零），则继续下一次迭代以生成有效的表达式。
            except ValueError as e:
                continue
            self.expressions.add(exp_string)
            self.expression_lists.append(exp_list)
            self.answers.append(str(answer))
            self.expression_num += 1

    def randomly_generate_questions(self):
        # 基于子表达式生成最终的问题。从头到尾处理子表达式，随机重新排列它们的顺序，
        # 并添加括号以创建问题字符串。根据两个相邻子表达式之间操作符的优先级来确定是否添加括号。
        for expression in self.expression_lists:
            op_1 = expression[0][1]
            if expression[0][1] in [' + ', ' * ']:
                if random.randint(0, 1):
                    question_1 = str(expression[0][0]) + str(expression[0][1]) + str(expression[0][2])
                else:
                    question_1 = str(expression[0][2]) + str(expression[0][1]) + str(expression[0][0])
            else:
                question_1 = str(expression[0][0]) + str(expression[0][1]) + str(expression[0][2])
            if len(expression) >= 2:
                if len(expression[1]) == 2:
                    if str(expression[1][0]) == ' + ':
                        op_2 = ' + '
                        if random.randint(0, 1):
                            question_2 = question_1 + op_2 + str(expression[1][1])
                        else:
                            if expression[0][1] in [' + ', ' - ']:
                                question_2 = str(expression[1][1]) + op_2 + '(' + question_1 + ')'
                            else:
                                question_2 = str(expression[1][1]) + op_2 + question_1
                    elif str(expression[1][0]) == ' * ':
                        op_2 = ' * '
                        if random.randint(0, 1):
                            if str(expression[0][1]) in [' * ', ' % ']:
                                question_2 = question_1 + op_2 + str(expression[1][1])
                            else:
                                question_2 = '(' + question_1 + ')' + op_2 + str(expression[1][1])
                        else:
                            question_2 = str(expression[1][1]) + op_2 + '(' + question_1 + ')'
                    elif str(expression[1][0]) == ' - ':
                        op_2 = ' - '
                        question_2 = question_1 + op_2 + str(expression[1][1])
                    elif str(expression[1][0]) == ' % ':
                        op_2 = ' % '
                        if str(expression[0][1]) in [' * ', ' % ']:
                            question_2 = question_1 + op_2 + str(expression[1][1])
                        else:
                            question_2 = '(' + question_1 + ')' + op_2 + str(expression[1][1])
                    elif str(expression[1][1]) == ' - ':
                        op_2 = ' - '
                        if str(expression[0][1]) in [' * ', ' % ']:
                            question_2 = str(expression[1][0]) + op_2 + question_1
                        else:
                            question_2 = str(expression[1][0]) + op_2 + '(' + question_1 + ')'
                    else:
                        op_2 = ' % '
                        question_2 = str(expression[1][0]) + op_2 + '(' + question_1 + ')'
                    if len(expression) > 2:
                        if expression[2][0] == ' + ':
                            op_3 = ' + '
                            if random.randint(0, 1):
                                question_3 = question_2 + op_3 + str(expression[2][1])
                            else:
                                if op_1 in [' + ', ' - '] and op_2 in [' + ', ' - ']:
                                    question_3 = str(expression[2][1]) + op_3 + '(' + question_2 + ')'
                                else:
                                    question_3 = str(expression[2][1]) + op_3 + question_2
                        elif expression[2][0] == ' - ':
                            op_3 = ' - '
                            question_3 = question_2 + op_3 + str(expression[2][1])
                        elif expression[2][0] == ' * ':
                            op_3 = ' * '
                            if random.randint(0, 1):
                                question_3 = str(expression[2][1]) + op_3 + '(' + question_2 + ')'
                            else:
                                if op_2 in [' * ', ' % ']:
                                    question_3 = question_2 + op_3 + str(expression[2][1])
                                else:
                                    question_3 = '(' + question_2 + ')' + op_3 + str(expression[2][1])
                        elif expression[2][0] == ' % ':
                            op_3 = ' % '
                            if op_2 in [' * ', ' % ']:
                                question_3 = question_2 + op_3 + str(expression[2][1])
                            else:
                                question_3 = '(' + question_2 + ')' + op_3 + str(expression[2][1])
                        elif expression[2][1] == ' - ':
                            op_3 = ' - '
                            if op_2 in [' * ', ' % ']:
                                question_3 = str(expression[2][0]) + op_3 + question_2
                            else:
                                question_3 = str(expression[2][0]) + op_3 + '(' + question_2 + ')'
                        elif expression[2][1] == ' % ':
                            op_3 = ' % '
                            question_3 = str(expression[2][0]) + op_3 + '(' + question_2 + ')'
                else:
                    question_1 = '(' + question_1 + ')'
                    question_2 = '(' + str(expression[1][0]) + str(expression[1][1]) + str(expression[1][2]) + ')'
                    if str(expression[2][0]) in [' + ', ' * ']:
                        if random.randint(0, 1):
                            question_3 = question_1 + str(expression[2][0]) + question_2
                        else:
                            question_3 = question_2 + str(expression[2][0]) + question_1
                    else:
                        question_3 = question_2 + str(expression[2][0]) + question_1
            if len(expression) == 1:
                self.questions.append(question_1)
            elif len(expression) == 2:
                self.questions.append(question_2)
            else:
                self.questions.append(question_3)

    def run(self):
        self.generate_expressions()
        self.randomly_generate_questions()
        return self.questions, self.answers
