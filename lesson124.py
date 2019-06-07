# 이진법
# 11/5 = 5 ... 1
#  5/2 = 2 ... 1
#  2/2 = 1 ... 0
#  1/2 = 0 ... 1
def digit(a,n):
    c = []
    while a // n != 0:
        e = a % n
        c.append(e)
        a //= n
    c.append(a)
    c.reverse()
    return c

print(digit(11,2))
# [1, 0, 1, 1]

