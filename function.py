import random

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

    def generate_subexpression(self,previous_value,etype,):
        operator=random.choice(['+','-','*','/'])
        ntype_1=random.randint(1,3)
        num_1=Number(ntype_1,self.max)
        ntype_2=random.randint(1,3)
        num_2=Number(ntype_2,self.max)
        if operator=='/':
            if num_1.get_value()<=num_2.get_value():
                return num_1.generate_string()+operator+num_2.generate_string
            else:
                return num_2.generate_string()+operator+num_1.generate_string
        else:
            if num_1.get_value()>num_2.get_value():
                return num_1.generate_string()+operator+num_2.generate_string
            else:
                return num_2.generate_string()+operator+num_1.generate_string
