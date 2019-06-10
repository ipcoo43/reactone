# 짝수(even), 홀수(odd) 판단하기

def isEven(num):
    if num % 2 == 0:
        return f'{num} 은 짝수'
    else:
        return f'{num} 은 홀수'

print(isEven(3))
print(isEven(4))
print()

def isOdd(num):
    if num % 2 == 1:
        return f'{num} 은 홀수'
    else:
        return f'{num} 은 짝수'
    
print(isEven(3))
print(isEven(4))