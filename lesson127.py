def is_prime(a):
    b = range(2,a)
    c = 0
    for i in b:
        if a % i == 0:
            c += 1
    if c > 0:
        d = False
    else:
        d = True
    return d

a = range(1,11) 
primes = [] # 소수 리스트를 공집합으로 만들고
for i in a: # 1부터 a-1까지 중,
    c = is_prime(i) # i가 소수이면 c = True, 아니면 False 생성
    if c == True:  # c가 True 이면
        primes.append(i) # primes에 i를 추가하라
print(primes) # [1, 2, 3, 5, 7]