def is_prime(a):
    b = range(2,a)
    c = 0
    for i in b:
        if a % i == 0:
            c += 1
    if c > 0:
        print(f'{a}는 소수가 아니다.')
        d = False
    else:
        print(f'{a}는 소수이다.')
        d = True
    return d

is_prime(17)