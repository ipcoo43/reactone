a = [3,1,4,2,9]
def even(n):
    if n % 2 == 0:
        return True
    else:
        return False

c = []
for i in a:
    if even(i):
        c.append(i)
print(c)

