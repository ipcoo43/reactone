def is_prime(a):
    b = range(2,a)  # 2부터 a-1까지
    c = 0
    for i in b: # b의 원소 i에 대해
        if a % i == 0: # a를 i 나눈 나머지가 0 이면
            c += 1     # c에 1을 더하라
    if c > 0: # c가 0보다 크면
        print('no prime') # 이 문장을 실행하고
        d = False # d에 False를 저장하고
    else: # 그렇지 않으면
        print('prime') # 이 문장을 실행하고
        d = True # d에 True를 저장하고
    return d # d를 돌려준다.

is_prime(13) # prime
is_prime(14) # no prime