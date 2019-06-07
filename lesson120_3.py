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
prime_numbers = []
for i in a:
    c = is_prime(i)
    if c == True:
        prime_numbers.append(i)
print(prime_numbers)