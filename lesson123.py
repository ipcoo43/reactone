'''
두수 a,b가 있을 때 a의 약수와 b의 공통된 약수 중 가장 큰 최대공약수
a의 배수와 b의 배수중 가장 작은수를 최소 공배수
- 최대공약수 구하는 과정
 - 두 수의 약수를 구하고
 - 두 약수의 교집합을 구하고
 - 교집합 중 가장 큰 숫자를 찾는다.
'''
def factorization(a):
    b = range(1,a)
    factors = []
    for i in b:
        if a % i == 0:
            factors.append(i)
    factors.append(i)
    return factors

def intersection(a,b):
    c = []
    for i in a:
        if i in b:
            c.append(i)
    return c

def greatest_common_factor(a,b,show=False):
    c = factorization(a) # a의 약수를 구해 c 리스트에 저장
    d = factorization(b) # b의 약수를 구해 d 리스트에 저장
    if show:             # show 가 true이면
        print(c)         # a의 약수인 c를 출력하고
        print(d)         # b의 약수인 d를 출력하고
    e = intersection(c,d) # c와 d의 교집합을 구한다
    return max(e)        # 최대값을 return 한다.

a,b=36,96
print(greatest_common_factor(a,b))
print(greatest_common_factor(a,b,show=True))
# show = True를 안쓰면 최대 공약수만 출력된다.
# 함수 정의 할 때 입력값 = 초기값을 미리 정의 해도 된다.