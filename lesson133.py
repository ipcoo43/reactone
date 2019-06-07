def is_prime(a):
    c = 0
    for b in range(2,a):
        if a % b == 0:
            c += 1
    if c > 0:
        d = False
    else:
        d = True
    return d

d = [x for x in range(1,11) if is_prime(x)]
print(d)