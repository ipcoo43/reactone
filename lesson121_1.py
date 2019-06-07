def prime_factorization(a):
    b = range(2,a)
    primes = []
    for i in b:
        while a % i == 0:
            primes.append(i)
            a /= i
    if primes == []:
        primes.append(a)
    return primes

print(prime_factorization(128)) # [2, 2, 2, 2, 2, 2, 2]
