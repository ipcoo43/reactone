'''
1부터 100까지 소수 중 소수와 그 다음 소수까지 차이가 가장 큰 구간
'''

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

a = range(2,11)
prime_numbers = [1]
diff = 0
for i in a:
    c = is_prime(i)
    if c == True:
        prime_numbers.append(i)
        if prime_numbers[-1] - prime_numbers[-2] > diff:
            diff = prime_numbers[-1] - prime_numbers[-2]
            max_diff_primes = [prime_numbers[-2], prime_numbers[-1]]
print(f'소수사이 구간의 최대값 : {diff}')
print(f'최대구간의 소수쌍 :{max_diff_primes}')