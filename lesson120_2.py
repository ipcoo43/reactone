def is_prime(a):
    b = range(2,a)      # 2부터 a-1까지
    c = 0               # c의 초기값은 0
    for i in b:         # b원소 i에 대해
        if a % i == 0:  # a를 i로 나눈 나머지가 0이면
            c += 1      # c에 1을 증가 시키고
    if c > 0:           # c가 0보다 크면
        d = False       # d는 False을 가지며
    else:               # 그렇지 않으면
        d = True        # d는 True값을 가진다.
    return d            # d의 값을 돌려준다

a = range(1,11)         # 1부터 10까지 지정한다
prime_numbers = []      # 소수 리스트를 공집합으로 만들고
for i in a:             # 1부터 10까지 중,
    c = is_prime(i)     # i가 소수이면 c는 True, 이니면 False 생성
    if c == True:       # c가 True이면
        prime_numbers.append(i) # 소수리스트에 i를 추가하라
print(prime_numbers)     