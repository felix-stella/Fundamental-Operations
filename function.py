import random
import math
from unittest import result

#def replace_characters(input_string):
#    # Replace * with ¡Á and % with ¡Â using the replace method
#    modified_string = input_string.replace('*', '¡Á').replace('%', '¡Â')
#    return modified_string

class Number:
    '''Generate number'''

    def __init__(self,max:int=None,nums:tuple=None):
        if nums:
            if isinstance(nums, tuple) and len(nums) == 3:
                if nums[2]==0:
                    raise ValueError("The denominator cannot be equal to 0.")
                else:
                    self.integer=int(nums[0])
                    self.numerator=int(nums[1])
                    self.denominator=int(nums[2])
            else:
                raise ValueError("nums must be a triplet (integer, numerator, denominator).")
        else:
            if (not isinstance(max,int)) or max<1:
                raise ValueError("max must not be less than 1.")
            self.integer=random.randint(0,max)
            self.denominator=random.randint(1,max)
            is_fra=random.randint(1,2)
            if is_fra==1:
                self.numerator=random.randint(1,self.denominator)
            else:
                self.numerator=0
    def reduce_fraction(self):
        gcd = math.gcd(self.numerator, self.denominator)
        numerator=self.numerator/gcd
        denominator=self.denominator/gcd
        integer=numerator//denominator+self.integer
        numerator=numerator%denominator
        self.integer=int(integer)
        self.numerator=int(numerator)
        self.denominator=int(denominator)


    def __str__(self):
        if self.integer==0:
            if self.numerator:
                return str(self.numerator)+'/'+str(self.denominator)
            else:
                return '0'
        else:
            if self.numerator:
                return str(self.integer)+'\''+str(self.numerator)+'/'+str(self.denominator)
            else:
                return str(self.integer)

    def __float__(self):
        return self.integer+self.numerator/self.denominator

class Fraction:
    '''Process fraction'''

    def __init__(self,f1:Number,f2:Number=None,op:str=None):
        if isinstance(f1,Number):
            self.f1=f1
        else:
            raise ValueError("The parameters must be of the Number type.")
        if f2:
            if isinstance(f2,Number):
                if op not in ['+','-','*','%']:
                    raise ValueError("The operator must be one of '+', '-', '', or '%'")
                self.f2=f2
                self.op=op
            else:
                raise ValueError("The parameters must be of the Number type.")

    #def reduce_fraction(self,f:Number):
    #    if isinstance(f,Number):
    #        gcd = math.gcd(f.numerator, f.denominator)
    #        numerator=f.numerator/gcd
    #        denominator=f.denominator/gcd
    #        integer=numerator//denominator+f.integer
    #        numerator=numerator%denominator
    #        result=Number(nums=(integer,numerator,denominator))
    #    else:
    #        raise ValueError("The parameters must be of the Number type.")
    #    return result
    
    def caculate_fractions(self):
        if self.f2:
            if self.op=='+':
                denominator=self.f1.denominator*self.f2.denominator
                numerator=(self.f1.integer*self.f1.denominator+self.f1.numerator)*self.f2.denominator\
                          +(self.f2.integer*self.f2.denominator+self.f2.numerator)*self.f1.denominator
                          
                result=Number(nums=(0,numerator,denominator))
            elif self.op=='-':
                denominator=self.f1.denominator*self.f2.denominator
                numerator=(self.f1.integer*self.f1.denominator+self.f1.numerator)*self.f2.denominator\
                          -(self.f2.integer*self.f2.denominator+self.f2.numerator)*self.f1.denominator
                result=Number(nums=(0,numerator,denominator))
            elif self.op=='*':
                denominator=self.f1.denominator*self.f2.denominator
                numerator=(self.f1.numerator+self.f1.integer*self.f1.denominator)\
                          *(self.f2.numerator+self.f2.integer*self.f2.denominator)
                result=Number(nums=(0,numerator,denominator))
            elif self.op=='%':
                if float(self.f2)==0:
                    raise ValueError("The divisor cannot be 0.")
                denominator=self.f1.denominator*(self.f2.numerator+self.f2.integer*self.f2.denominator)
                numerator=(self.f1.numerator+self.f1.integer*self.f1.denominator)*self.f2.denominator
                result=Number(nums=(0,numerator,denominator))

        else:
            result=self.f1
        result.reduce_fraction()
        return result


class Expression:
    '''Generate arithmetic expressions.'''

    def __init__(self,max,question_num):
        self.max=max
        self.question_num=question_num
        self.expressions=set()
        self.expression_lists=[]
        self.generation_times=0
        self.answers=[]
        self.questions=[]
        self.expression_num=0

    def caculate_subexpression(self,num_1,operator,num_2):
        if operator=='+':
            return num_1+num_2
        elif operator=='-':
            return num_1-num_2
        elif operator=='*':
            return num_1*num_2
        else:
            return num_1/num_2

    def generate_subexpression(self,etype,op):
        if etype==1:
            num_1=Number(self.max)
            num_1.reduce_fraction()
            num_2=Number(self.max)
            num_2.reduce_fraction()
            if op !='%':
                if float(num_1)>=float(num_2):
                    subexpression=[num_1,op,num_2]
                else:
                    subexpression=[num_2,op,num_1]
            else:
                subexpression=[num_1,op,num_2]
        else :
            if op in ['-','%']:
                if random.randint(0,1):
                    num=Number(self.max)
                    num.reduce_fraction()
                    subexpression=[op,num]
                else:
                    num=Number(self.max)
                    num.reduce_fraction()
                    subexpression=[num,op]
            else:
                num=Number(self.max)
                num.reduce_fraction()
                subexpression=[op,num]
        return subexpression

    def generate_expression_list(self):
        expression_list=[]
        sub_num=random.randint(1,3)
        operators=[random.choice(['+','-','*','%']) for _ in range(sub_num)]
        subexpression_1=self.generate_subexpression(1,operators[0])
        str_sub_1=str(subexpression_1[0])+subexpression_1[1]+str(subexpression_1[2])
        if sub_num==1:
            expression_list.append(subexpression_1)
            str_sub_2=''
            str_sub_3=''
            string=str_sub_1+'|'+str_sub_2+'|'+str_sub_3
        elif sub_num==2:
            subexpression_2=self.generate_subexpression(2,operators[1])
            str_sub_2=str(subexpression_2[0])+str(subexpression_2[1])
            str_sub_3=''
            expression_list.append(subexpression_1)
            expression_list.append(subexpression_2)
            string=str_sub_1+'|'+str_sub_2+'|'+str_sub_3
        else :
            etype=random.randint(1,2)
            subexpression_2=self.generate_subexpression(etype,operators[1])
            if etype==1:
                subexpression_3=[operators[2]]
                str_sub_2=str(subexpression_2[0])+str(subexpression_2[1])+str(subexpression_2[2])
                str_sub_3=subexpression_3[0]
                if str_sub_1>=str_sub_2 and operators[2] in ['+','*']:
                    expression_list.append(subexpression_1)
                    expression_list.append(subexpression_2)  
                    expression_list.append(subexpression_3)
                    string=str_sub_1+'|'+str_sub_2+'|'+str_sub_3
                else:
                    expression_list.append(subexpression_2)
                    expression_list.append(subexpression_1)  
                    expression_list.append(subexpression_3)
                    string=str_sub_1+'|'+str_sub_2+'|'+str_sub_3
            else:
                subexpression_3=self.generate_subexpression(2,operators[2])
                str_sub_2=str(subexpression_2[0])+str(subexpression_2[1])
                str_sub_3=str(subexpression_3[0])+str(subexpression_3[1])
                expression_list.append(subexpression_1)
                expression_list.append(subexpression_2)  
                expression_list.append(subexpression_3)
                string=str_sub_1+'|'+str_sub_2+'|'+str_sub_3
        return expression_list,string

    def caculate_answer(self,expression_list):
        expression_1=Fraction(expression_list[0][0],expression_list[0][2],expression_list[0][1])
        result_1=expression_1.caculate_fractions()
        if float(result_1)<0:
            raise ValueError("Sub expression cannot be less than zero.")
        if len(expression_list)==1:
            result=result_1
        elif len(expression_list)==2:
            if isinstance(expression_list[1][0],str):
                expression_2=Fraction(result_1,expression_list[1][1],expression_list[1][0])
            else:
                expression_2=Fraction(expression_list[1][0],result_1,expression_list[1][1])
            result=expression_2.caculate_fractions()
        else:
            if len(expression_list[2])==1:
                expression_2=Fraction(expression_list[1][0],expression_list[1][2],expression_list[1][1])
                result_2=expression_2.caculate_fractions()
                if float(result_2)<0:
                    raise ValueError("Sub expression cannot be less than zero.")
                expression_3=Fraction(result_1,result_2,expression_list[2][0])
                result=expression_3.caculate_fractions()
            else:
                if isinstance(expression_list[1][0],str):
                    expression_2=Fraction(result_1,expression_list[1][1],expression_list[1][0])
                else:
                    expression_2=Fraction(expression_list[1][0],result_1,expression_list[1][1])
                result_2=expression_2.caculate_fractions()
                if float(result_2)<0:
                    raise ValueError("Sub expression cannot be less than zero.")
                if isinstance(expression_list[2][0],str):
                    expression_2=Fraction(result_2,expression_list[2][1],expression_list[2][0])
                else:
                    expression_2=Fraction(expression_list[2][0],result_2,expression_list[2][1])
                result=expression_2.caculate_fractions()
        if float(result)<0:
            raise ValueError("Sub expression cannot be less than zero.")
        return result

    def generate_expressions(self):
        while(self.expression_num<self.question_num):
            self.generation_times+=1
            try:
                exp_list,exp_string=self.generate_expression_list()
                answer=self.caculate_answer(exp_list)
            except ValueError as e:
                continue
            self.expressions.add(exp_string)
            self.expression_lists.append(exp_list)
            self.answers.append(str(answer))
            self.expression_num+=1

    def randomly_generate_questions(self):
        for expression in self.expression_lists:
            op_1=expression[0][1]
            if expression[0][1] in ['+','*']:
                if random.randint(0,1):
                    question_1=str(expression[0][0])+str(expression[0][1])+str(expression[0][2])
                else:
                    question_1=str(expression[0][2])+str(expression[0][1])+str(expression[0][0])
            else:
                question_1=str(expression[0][0])+str(expression[0][1])+str(expression[0][2])
            if len(expression)>=2 :
                if len(expression[1])==2:
                    if str(expression[1][0])=='+':
                        op_2='+'
                        if random.randint(0,1):
                            question_2=question_1+op_2+str(expression[1][1])
                        else:
                            if expression[0][1] in ['+','-']:
                                question_2=str(expression[1][1])+op_2+'('+question_1+')'
                            else:
                                question_2=str(expression[1][1])+op_2+question_1
                    elif str(expression[1][0])=='*':
                        op_2='*'
                        if random.randint(0,1):
                            if str(expression[0][1]) in ['*','%']:
                               question_2=question_1+op_2+str(expression[1][1])
                            else:
                                question_2='('+question_1+')'+op_2+str(expression[1][1])
                        else:
                            question_2=str(expression[1][1])+op_2+'('+question_1+')'
                    elif str(expression[1][0])=='-':
                        op_2='-'
                        question_2=question_1+op_2+str(expression[1][1])
                    elif str(expression[1][0])=='%':
                        op_2='%'
                        if str(expression[0][1]) in ['*','%']: 
                            question_2=question_1+op_2+str(expression[1][1])
                        else:
                            question_2='('+question_1+')'+op_2+str(expression[1][1])
                    elif str(expression[1][1])=='-':
                        op_2='-'
                        if str(expression[0][1]) in ['*','%']: 
                            question_2=str(expression[1][0])+op_2+question_1
                        else:
                            question_2=str(expression[1][0])+op_2+'('+question_1+')'
                    else:
                        op_2='%'
                        question_2=str(expression[1][0])+op_2+'('+question_1+')'
                    if len(expression)>2:
                        if expression[2][0]=='+':
                            op_3='+'
                            if random.randint(0,1):
                                question_3=question_2+op_3+str(expression[2][1])
                            else:
                                if op_1 in ['+','-'] and op_2 in ['+','-']:
                                    question_3=str(expression[2][1])+op_3+'('+question_2+')'
                                else:
                                    question_3=str(expression[2][1])+op_3+question_2
                        elif expression[2][0]=='-':
                            op_3='-'
                            question_3=question_2+op_3+str(expression[2][1])
                        elif expression[2][0]=='*':
                            op_3='*'
                            if random.randint(0,1):
                                question_3=str(expression[2][1])+op_3+'('+question_2+')'
                            else:
                                if op_2 in ['*','%']:
                                    question_3=question_2+op_3+str(expression[2][1])
                                else:
                                    question_3='('+question_2+')'+op_3+str(expression[2][1])
                        elif expression[2][0]=='%':
                            op_3='%'
                            if op_2 in ['*','%']:
                                question_3=question_2+op_3+str(expression[2][1])
                            else:
                                question_3='('+question_2+')'+op_3+str(expression[2][1])
                        elif expression[2][1]=='-':
                            op_3='-'
                            if op_2 in ['*','%']:
                                question_3=str(expression[2][0])+op_3+question_2
                            else:
                                question_3=str(expression[2][0])+op_3+'('+question_2+')'
                        elif expression[2][1]=='%':
                            op_3='%'
                            question_3=str(expression[2][0])+op_3+'('+question_2+')'
                else:
                    question_1='('+question_1+')'
                    question_2='('+str(expression[1][0])+str(expression[1][1])+str(expression[1][2])+')'
                    if str(expression[2][0]) in ['+','*']:
                        if random.randint(0,1):
                            question_3=question_1+str(expression[2][0])+question_2
                        else:
                            question_3=question_2+str(expression[2][0])+question_1
                    else:
                        question_3=question_2+str(expression[2][0])+question_1
            #if len(expression)==1:
            #    question=replace_characters(question_1)
            #elif len(expression)==2:
            #    question=replace_characters(question_2)
            #else:
            #    question=replace_characters(question_3)
            #self.questions.append(question)
            if len(expression)==1:
                self.questions.append(question_1)
            elif len(expression)==2:
                self.questions.append(question_2)
            else:
                self.questions.append(question_3)


    def run(self):
        self.generate_expressions()
        self.randomly_generate_questions()
        return self.questions,self.answers


exp=Expression(5,10000)
questions,answers=exp.run()
with open('./question', "w") as file:
    for question in questions:
        file.write(question + "\n")
with open('./answer', "w") as file:
    for answer in answers:
        file.write(answer + "\n")
