'''
최소공배수 구하기 과정
 - 두 수의 소인수분해하기
 - 두 수 소인수를 다 곱하지만 공통된 약수는 한번만 곱하기 
12, 18의 최소 공배수
 - 두 수 소인수 분해
   12 = 2,2,3
   18 = 2,3,3
 - 2,3은 공통된 소인수 이므로 
 - 최소 공배수 = 2 * 2 * 3 * 3 = 36
'''

def prime_factorization(a):
    b = range(2,a)
    primes = []
    for i in b:
        while a % i ==0:
            primes.append(i)
            a /= i
    if primes == []:
        primes.append(i)
    return primes

print(prime_factorization(36)) # [2, 2, 3, 3]
print(prime_factorization(96)) # [2, 2, 2, 2, 2, 3]

def least_common_multiple(a,b):
    c = prime_factorization(a) # a의 소인수 구해 c 리스트에 저장
    d = prime_factorization(b) # b의 소인수 구해 d 리스트에 저장
    for i in c: 
        if i in d: # c와 d의 공통원소이면 
            d.remove(i) # 1개만 취한다.
    e = c + d # a,b인 소인수들의 합집합인 소인수분대를 구한다
    f = 1
    for i in e: # e의 모든 원소에 대해
        f *= i  # f에다가 계속 곱해라
    return f
print (least_common_multiple(36,96))
print (least_common_multiple(4,7))
