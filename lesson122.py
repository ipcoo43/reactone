'''
약수 (factor) 구하기
'''
a = 24
b = range(1,a)  # 1부터 a-1까지 자연수 집합
factors = []    # 약수 리스트를 공집합으로 만들고
for i in b:     # 1부터 a-1까지 원소 i에 대해
    if a % i == 0: # a를 i로 나눈 나머지가 0이면
        factors.append(i) # 약수집에에 i를 추가하여라
factors.append(a)  # 자기 자신인 a를 추가하여라
print(factors) # [1, 2, 3, 4, 6, 8, 12, 24]