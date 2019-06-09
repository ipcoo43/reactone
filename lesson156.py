# 1부터 n까지 연속한 숫자의 제곱의 합 구하기
# 입력 : n = 10
# 과정 : 1**2 + 2**2 + 3**2 ... n**2 
# 출력 : 385

def sum_one(n):
    s = 0
    for i in range(1,n+1):
        s = s + (i**2)
    return s

print(sum_one(10))

def sum_two(n):
    return n*(n+1)*(2*n+1)/6

print(sum_two(10))