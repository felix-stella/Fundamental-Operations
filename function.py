import random
import math

class Number:
    '''Generate proper fractions, whole numbers, mixed fractions.
    1 stands for proper fractions, 2 stands for mixed fractions,
    others stand for whole numbers.'''

    def __init__(self,ntype,max,min=0):
        self.integer=0
        self.numerator=0
        self.denominator=0
        self.ntype=ntype
        if self.ntype==1:
            if max<2:
                self.ntype=3
                self.integer=random.randint(min,max)
            else:
                self.denominator=random.randint(2,max)
                self.numerator=random.randint(1,self.denominator-1)
        elif self.ntype==2:
            if max<2:
                self.ntype=3
                self.integer=random.randint(min,max-1)
                return
            else:
                self.integer=random.randint(min,max-1)
                self.denominator=random.randint(2,max)
                self.numerator=random.randint(1,self.denominator-1)
        else:
            self.ntype=3
            self.integer=random.randint(min,max)

    def generate_string(self):
        if self.ntype==1:
            return str(self.numerator)+'/'+str(self.denominator)
        elif self.ntype==2:
            return str(self.integer)+'\''+str(self.numerator)+'/'+str(self.denominator)
        else:
            return str(self.integer)

    def get_value(self):
        if self.denominator:
            return self.integer+self.numerator/self.denominator
        else:
            return self.integer

    def get_ntype(self):
        return self.ntype

class Expression:
    '''Generate arithmetic expressions.'''

    def __init__(self,max,question_num):
        self.max=max
        self.question_num=question_num

    def caculate_subexpression(self,num_1,operator,num_2):
        if operator=='+':
            return num_1+num_2
        elif operator=='-':
            return num_1-num_2
        elif operator=='*':
            return num_1*num_2
        else:
            return num_1/num_2

    def generate_subexpression(self,etype,previous_value=0):
        operator=random.choice(['+','-','*','/'])
        if etype==1:
            ntype_1=random.randint(1,3)
            num_1=Number(ntype_1,self.max)
            ntype_2=random.randint(1,3)
            num_2=Number(ntype_2,self.max)
            if operator=='/':
                subexpression=num_1.generate_string()+operator+num_2.generate_string
            else:
                if num_1.get_value()>num_2.get_value():
                    subexpression=num_1.generate_string()+operator+num_2.generate_string
                else:
                    subexpression=num_2.generate_string()+operator+num_1.generate_string
            return subexpression,self.caculate_subexpression(num_1.get_value(),operator,num_2.get_value())
        elif etype==2:
            if operator=='-':
                n_max=math.floor(previous_value)
                num=Number(random.randint(1,3),n_max)
                subexpression=operator+num.generate_string()
            elif operator=='/':
                num=Number(random.randint(1,3),self.max,1)
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
            etype_1=1
            subexpression_1,value_1=self.generate_subexpression(etype_1)
            etype_2=random.randint(1,2)
            subexpression_2,value_2=self.generate_subexpression(etype_2,value_1)

            if etype_2==1:
                etype_3=3
                subexpression_3,value_3=self.generate_subexpression(etype_3)
            else:
                etype_3=2
                subexpression_3,value_3=self.generate_subexpression
                (etype_2,self.caculate_subexpression(value_1,subexpression_2[0],value_2))

            if etype_3==3:
                if subexpression_3=='-':
                    if(value_1<value_2):
                        generated=0
                    else:
                        expression_list.append(subexpression_1)
                        expression_list.append(subexpression_2)
                        expression_list.append(subexpression_3)
                        generated=1
                elif subexpression_3=='/':
                    if value_2==0:
                        generated=0
                    else:
                        expression_list.append(subexpression_1)
                        expression_list.append(subexpression_2)
                        expression_list.append(subexpression_3)
                        generated=1
                else:
                    if subexpression_1>subexpression_2:
                        expression_list.append(subexpression_1)
                        expression_list.append(subexpression_2)
                        expression_list.append(subexpression_3)
                    else:
                        expression_list.append(subexpression_2)
                        expression_list.append(subexpression_1)
                        expression_list.append(subexpression_3)
            else:
                    expression_list.append(subexpression_2)
                    expression_list.append(subexpression_1)
                    expression_list.append(subexpression_3)
                    generated=1
        return expression_list


