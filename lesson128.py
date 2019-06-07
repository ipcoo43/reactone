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

a = range(2,11) # 2부터 11까지 지정
b = [1] # 소수 리스트를 1부터 시작하는 리스트 생성
d = 0   # 소수와 그 다음 소수까지 차이를 우선 0으로 만들고
for i in a: # 2부터 10까지 중
    c = is_prime(i) # i가 소수이면 True, 아니면 False 생성
    if c == True:   # c가 True이면
        b.append(i) # b에 i를 추가하라
        if b[-1] - b[-2] > d: # 추가된 마지막 - 그 앞을 뺀수가 d보다 크면
            d = b[-1] - b[-2] # 추가된 마지막 - 그 앞을 뺀수를 d에 저장하고
            max_d = [b[-2],b[-1]] # 마지막 앞 수와 마지막수를 max_d에 저장
print(d) # 2
print(max_d) # [3,5]