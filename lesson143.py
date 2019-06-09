from fractions import Fraction

def linear_eq_one(a,b,c):
    x = Fraction((c-b),a)
    return x
print(linear_eq_one(2,-3,5))

def linear_eq_two(a,b,c):
    x = Fraction((c-b),a)
    if x.denominator == 1:
        x = int(Fraction(x))
    return x
print(linear_eq_two(2,-3,5))

# 일차함수의 계수 a가 0이고 b = c 일때 해는 무수히 많다
# 일차함수의 계수 a가 0이고 b != c 일때 해는 없다
 
def linear_eq(a,b,c):
    if a == 0:
        if b == c:
            print('해는 무수히 많다')
            return
        else:
            print('해는 없다.')
            return
    else:
        x = Fraction((c-b),a)
        if x.denominator == 1:
            x = int(Fraction(x))
        return x
linear_eq(2,-3,5)
linear_eq(0,3,4)
linear_eq(0,3,3)
