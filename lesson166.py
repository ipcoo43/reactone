# 최대공약수(Greates Common Divisor, GCD) 구하기
# - 두 수 약수 중에서 가장 큰 값을 의미
# 두 자연수 a,b의 최대 공약수 구하기
# - 두 수 약수 구하고
# - 약수 중에서 공통된 것을 찾아
# - 그 값 중에서 최대값인 것을 찾아야 한다.
# - 역순으로 읽으면 최대공약수

# [ 알고리즘 ]
# - 두 수 중 더 작은 값을 i에 저장
# - i가 두 수의 공통된 약수인지 판단
# - 공통된 약수이면 이 값을 결과값으로 돌려주고 종료
# - 공통된 약수가 아니면 i를 1만큼 감소시키고 
# - i가 두 수의 공통된 약수인지 판단으로 돌아가 반복한다
# - 1은 모든 정수의 약수이므로 i가 1이 되면 1을 결과값으로 돌려주고 종료

# 4와 6의 최대공약수
# i에 4를 저장한다(4와 6중 작은 값인 4가 최대공약수 후보 중 가장 큰 값)
# 4를 i로 나눠 떨어지지만, 6은 나눠어 떨어지지 않는다.
# i를 1만큼 감소시켜 3으로 만든다
# 4는 i로 나누어 떨어지지 않는다.
# i를 1만큼 감소시켜 2로 만든다
# 4,6모두 i로 나누어 떨이지므로 i값 2가 최대 공약수이다.

def gcd(a,b):
    i = min(a,b) # 두 수 중에서 최소값을 구하는 함수
    while True:
        if (a%i == 0) and (b%i == 0): # % 나머지 연산자
            return i
        i = i - 1 # i를 1만큼 감소
print(gcd(1,5))
print(gcd(3,6))
print(gcd(60,24))
