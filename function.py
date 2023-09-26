import random
import math

class Number:
    '''Generate number'''

    def __init__(self,max=None,nums=None):
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

    def generate_string(self):
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

    def get_value(self):
        return self.integer+self.numerator/self.denominator

class Fraction:
    '''Process fraction'''

    def __init__(self,f1,f2=None,op=None):
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

    def reduce_fraction(self,f):
        if isinstance(f,Number):
            gcd = math.gcd(f.numerator, f.denominator)
            numerator=f.numerator/gcd
            denominator=f.denominator/gcd
            integer=f.integer
            if numerator>=0:
                if(numerator>=denominator):
                    integer=numerator//denominator+f.integer
                    numerator=numerator%denominator
            else:
                if(-numerator>=denominator):
                    integer=-((-numerator)//denominator)
                    numerator=-((-numerator)%denominator)
            result=Number(nums=(integer,numerator,denominator))
        else:
            raise ValueError("The parameters must be of the Number type.")
        return result
    
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
                denominator=self.f1.denominator*(self.f2.numerator+self.f2.integer*self.f2.denominator)
                numerator=(self.f1.numerator+self.f1.integer*self.f1.denominator)*self.f2.denominator
                result=Number(nums=(0,numerator,denominator))

        else:
            result=self.f1
        result=self.reduce_fraction(result)
        return result


class Expression:
    '''Generate arithmetic expressions.'''

    def __init__(self,max,question_num):
        self.max=max
        self.question_num=question_num
        self.expressions=set()
        self.expression_lists=[]

    def caculate_subexpression(self,num_1,operator,num_2):
        if operator=='+':
            return num_1+num_2
        elif operator=='-':
            return num_1-num_2
        elif operator=='*':
            return num_1*num_2
        else:
            return num_1/num_2

    def generate_subexpression(self,etype,min_value=-1):
        operator=random.choice(['+','-','*','%'])
        if etype==1:
            ntype_1=random.randint(1,3)
            num_1=Number(ntype_1,self.max)
            ntype_2=random.randint(1,3)
            num_2=Number(ntype_2,self.max)
            if operator=='%':
                num_value=0
                while(num_2.get_value==0):
                    num_2=Number(ntype_2,self.max)
                    num_value=num.get_value()
                if min_value>=0:
                    num_1=Number(ntype_1,self.max,math.ceil(num_value*min_value))
                subexpression=num_1.generate_string()+operator+num_2.generate_string()
            elif operator=='-':
                if min_value>=0:
                    num_1=Number(ntype_1,self.min_value)
                    subexpression=num_1.generate_string()+operator+num_2.generate_string()
                else:
                    if num_1.get_value()>num_2.get_value():
                        subexpression=num_1.generate_string()+operator+num_2.generate_string()
                    else:
                        subexpression=num_2.generate_string()+operator+num_1.generate_string()
            elif operator=='*':
                if min_value>0:
                    num_value=0
                    while(num_2.get_value==0):
                        num_2=Number(ntype_2,self.max)
                        num_value=num.get_value()
                    num_1=Number(ntype_1,self.max,math.ceil(min_value/num_value))
                if num_1.get_value()>num_2.get_value():
                    subexpression=num_1.generate_string()+operator+num_2.generate_string()
                else:
                    subexpression=num_2.generate_string()+operator+num_1.generate_string()
            else:
                if min_value>0:
                    num_1=Number(ntype_1,self.max,math.ceil(min_value-num_value))
                if num_1.get_value()>num_2.get_value():
                    subexpression=num_1.generate_string()+operator+num_2.generate_string()
                else:
                    subexpression=num_2.generate_string()+operator+num_1.generate_string()
            return subexpression,self.caculate_subexpression(num_1.get_value(),operator,num_2.get_value())
        elif etype==2:
            if operator=='%':
                num_value=0
                while(num_value==0):
                    num=Number(random.randint(1,3),self.max)
                    num_value=num.get_value()
                subexpression=operator+num.generate_string()
            else:
                num=Number(random.randint(1,3),self.max)
                subexpression=operator+num.generate_string()
            return subexpression,num.get_value()
        else:
            subexpression=operator
            return subexpression,-1

    def generate_expression_list(self):
        generated=0
        while(not generated):
            expression_list=[]
            sub_num=random.randint(1,3)
            if sub_num==1:
                etype_1=1
                subexpression_1,value_1=self.generate_subexpression(etype_1)
                expression_list.append(subexpression_1)
                generated=1
            elif sub_num==2:
                etype_2=2
                subexpression_1,value_1=self.generate_subexpression(etype_1)
                if subexpression_1[0]=='-':
                    min_value=value_1
                else:
                    min_value=-1
                etype_2=1
                subexpression_2,value_2=self.generate_subexpression(etype_2,min_value)
                expression_list.append(subexpression_1)
                expression_list.append(subexpression_2)
                generated=1
            else:
                etype_3=random.randint(2,3)
                subexpression_3,value_3=self.generate_subexpression(etype_3)
                if(etype_3==3):
                    etype_2=1
                    etype_1=1
                    if subexpression_3=='%':
                        subexpression_2,value_2=self.generate_subexpression(etype_2)
                        while(value_2==0):
                            subexpression_2,value_2=self.generate_subexpression(etype_2)
                    if subexpression_3=='-':
                        subexpression_1,value_1=self.generate_subexpression(etype_1,value_2)
                else:
                    etype_2=2
                    etype_1=1
                    subexpression_2,value_2=self.generate_subexpression(etype_2)
                    if subexpression_3[0]=='-':
                        if subexpression_2[0]=='+':
                            subexpression_1,value_1=self.generate_subexpression(etype_1,value_2)
        #        if etype_2==1:
        #            etype_3=3
        #            subexpression_3,value_3=self.generate_subexpression(etype_3)
        #        else:
        #            etype_3=2
        #            subexpression_3,value_3=self.generate_subexpression(etype_3,value_2)
        #            (etype_2,self.caculate_subexpression(value_1,subexpression_2[0],value_2))

        #        if etype_3==3:
        #            if subexpression_3=='-':
        #                if(value_1<value_2):
        #                    generated=0
        #                else:
        #                    expression_list.append(subexpression_1)
        #                    expression_list.append(subexpression_2)
        #                    expression_list.append(subexpression_3)
        #                    generated=1
        #            elif subexpression_3=='%':
        #                if value_2==0:
        #                    generated=0
        #                else:
        #                    expression_list.append(subexpression_1)
        #                    expression_list.append(subexpression_2)
        #                    expression_list.append(subexpression_3)
        #                    generated=1
        #            else:
        #                if subexpression_1>subexpression_2:
        #                    expression_list.append(subexpression_1)
        #                    expression_list.append(subexpression_2)
        #                    expression_list.append(subexpression_3)
        #                else:
        #                    expression_list.append(subexpression_2)
        #                    expression_list.append(subexpression_1)
        #                    expression_list.append(subexpression_3)
        #        else:
        #                expression_list.append(subexpression_1)
        #                expression_list.append(subexpression_2)
        #                expression_list.append(subexpression_3)
        #                generated=1
        #expression_string=','.join(expression_list)
        #if expression_string not in self.expressions:
        #    self.expressions.add(expression_string)
        #    self.expression_lists.append(expression_list)
        #return expression_list
    
    def generate_questions_set(self):
        while(len(self.expressions)<self.question_num):
            self.generate_expression_list()

    def process_string(self,string):
        operators=['+','-','*','%']
        num_1=''
        num_2=''
        operator=''
        if string[0] in operators:
            operator=string[0]
            num_1=''
            num_2=string[1:]
            etype=2
        elif string[-1] in operators:
            operator=string[-1]
            num_1=string[:-1]
            num_2=''
            etype=3
        else:
            etype=1
            for op in operators:
                index = string.find(op)
                if index != -1:
                    operator = string[index]
                    num_1=string[index]
                    num_2=string[index+1:]
                    break
        return etype,[num_1,operator,num_2]

    def process_fraction(self,num):
        fra_bar_index=num.find('/')
        if fra_bar_index !=-1:
            denominator=int(num[fra_bar_index+1:])
            delimiter_index=num.find('\'')
            if delimiter_index !=-1:
                integer=int(num[:delimiter_index])
                numerator=int(num[delimiter_index+1:fra_bar_index])+integer*denominator
            else:
                numerator=int(num[:delimiter_index])
        else:
            denominator=1
            numerator=int(num)
        
        return [numerator,denominator]
    def caculate_frations(self,num_1,operator,num_2):
        if operator=='+':
            numerator=num_1[0]*num_2[1]+num_2[0]*num_1[1]
            denominator=num_1[1]*num_2[1]
        elif operator=='-':
            numerator=num_1[0]*num_2[1]-num_2[0]*num_1[1]
            denominator=num_1[1]*num_2[1]
        elif operator=='*':
            numerator=num_1[0]*num_2[0]
            denominator=num_1[1]*num_2[1]
        else:
            numerator=num_1[0]*num_2[1]
            denominator=num_1[1]*num_2[0]
        return [numerator,denominator]
    
    def caculate_answer(self,expression_list):
        answer=[]
        for subexp in expression_list:
            processed_subexp=self.process_string(subexp)
            if processed_subexp[0]:
                num_1=self.process_fraction(processed_subexp[0])
                num_2=self.process_fraction(processed_subexp[2])
                answer.append(self.caculate_frations(num_1,processed_subexp[1],num_2))
            elif processed_subexp[2]!='':
                num_2=self.process_fraction(processed_subexp[2])
                answer.append(self.caculate_frations(answer[-1],processed_subexp[1],num_2))
            else:
                answer.append(self.caculate_frations(answer[-2],processed_subexp[1],answer[-1]))
        return answer[-1]

#for i in range(1000):
#    a=Expression(10,1)
#    t=a.generate_expression_list()
#    print(t)

a=Number(nums=(0,1,3))
b=Number(nums=(0,9,2))
c=Fraction(a,b,'-')
result=c.caculate_fractions()
print(result.generate_string())
print(result.get_value())