# 유클리드 최대공약수
# 입력 : a,b
# 출력 : a,b의 최대공약수
# gcd(a,b)=gcd(b,a%b) # b,a를 b로 나눈 나머지
# gcd(a,0)=a # 어떤 수와 0의 최대공약수는 자기 자신

def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a%b)
print(gcd(60,24))

# 재귀호출
# gcd(60,24)
# gcd(24,60%24)
# gcd(24,12)
# gcd(12,24%12)
# gcd(12,0)
# 12