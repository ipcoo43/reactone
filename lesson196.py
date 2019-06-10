# Bubble Sort
# 자리 바꾸기
# 규칙 찾기
# 반복문 적용하기
# 또 다른 규칙 적용하기

numbers = [7, 3, 2, 9,4]

# 0번째와 나머지를 모두 비교한다. 1바퀴
# 가장 작으게 0번째
# 그 다음으로 작은게 1번째 오게 해야 한다.
# 0 1 2
# 0: 1, 2, 3
# 1: 2, 3
# 2: 3
for idx in range(0,len(numbers)-1): # 0,1,2
    for i in range(idx+1,len(numbers)): # 1,2,3
        if numbers[idx] > numbers[i]:
            temp = numbers[idx]
            numbers[idx] = numbers[i]
            numbers[i] = temp
        print(numbers) # 6번 실행

# n = 1
# 1 2 n, n+1
# 1 3 n, n+1
# 0 1 2