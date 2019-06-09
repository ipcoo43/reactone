from fractions import Fraction
import numpy as np

def linear_eq(a,b,c):
    if a == 0:
        if b == c:
            print('해는 무수히 많다')
            return
        else:
            print('해는 없다')
            return
    else:
        x = Fraction((c-b),a)
        if x.denominator == 1:
            x = int(Fraction(x))
        return x
        
class Linear_equation:
    def question(self):
        self.coefficient = np.random.randint(-10,10)
        self.constant1 = np.random.randint(-20,20)
        self.constant2 = np.random.randint(-20,20)
        self.pm = np.random.randint(2)
        if self.pm == 0:
            print(f'{self.coefficient}x + {self.constant1} = {self.constant2}')
        elif self.pm == 1:
            print(f'{self.coefficient}x - {self.constant1} = {self.constant2}')
    
    def answer(self):
        if self.pm == 1:
            self.constant1 *= -1
        x = linear_eq(self.coefficient,self.constant1,self.constant2)
        return x

q1 = Linear_equation()        
q1.question()
print(q1.answer())
