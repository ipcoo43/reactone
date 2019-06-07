a=17
a_prime = True
for i in range(2,a):
    if a % i ==0:
        a_prime = False
if a_prime == True:
    print(f'{a}는 소수이다.')
else:
    print(f'{a}는 소수가 아니다.')