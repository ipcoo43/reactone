# prime : 1과 자기자신밖에 안 나누어지는 수
# 자기자신을 2부터 자기자신-1로 나눠 나머지가 0인지 판별
a = 17
b = range(2,a) # 2부터 a-1까지
c = True # 초기값 True 설정
for i in b: # b의 원소 i에대해
    if a % i == 0: # a를 i로 나눈 나머지가 0이면
        c = False  # c를 False로 바꿔라
if c == True: # c가 True이면
    print('prime')
else: # 그렇지 않으면
    print('no prime')    