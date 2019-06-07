def factorization(a):
    b = range(1,a)
    factors = []
    for i in b:
        if a % i == 0:
            factors.append(i)
    factors.append(a)
    return factors
print(factorization(36)) # [1, 2, 3, 4, 6, 9, 12, 18, 36]