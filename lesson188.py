# 짝수, 홀수 인지 판단하기
# 짝수(even)이면 True 홀수(odd)이면 Fasle
# 홀수, 짝수 판단하는 로직 왜 만들까?
# 구글 검색 했을 때 다른 로직에 포함되어 있음
# 4라는 숫자 2로 나누면 = 몫(quota) : 2, 나머지(remainder) : 0
# 10 / 2 = q:5,re:0
# 11 / 2 = q:5 re:1 
# 12 / 2 = q:6, re:0
# 1212122122 = q:_ ,re:0
# 13 / 2 = q:6, re:1  
# 12121213 / 2 = q:_, re:1
# 13131313 / 2 = q:_, re:1  

def isEven(num):
    # 홀수인지 짝수인지 판단
    # 2로 나눠서 '나머지' 판단
    zero = num % 2 == 0
    one = num % 2 == 1
    print(f'{num} % 2 == 0 :', zero)
    print(f'{num} % 2 == 1 :', one)
    
    # 짝수면 True, 홀수면 False
    if num % 2 == 0:
        return f"{num} 은 짝수이다"
    else:
        return f"{num} 은 홀수이다"

result = isEven(3)
print(result)