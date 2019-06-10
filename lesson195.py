# Bubble Sort
# [ 핵심 로직 ] n, n+1
# 1) 첫 번째, 두번째 비교 해서 두번째 더 작은면 첫 번째와 자리 바꿈
# 2) 규칙 찾기

# n = 1
# numbers = [7,3,2,9] # 
# numbers = [3,7,2,9] # n n+1 = 1,2
# numbers = [2,7,3,9] # n n+2 = 1,3
# numbers = [2,7,3,9] # n n+3 = 1,4

# 비교해서 뒤에게 작으면 바꾼다

numbers = [7,3,2,9] 

for i in range(1,len(numbers)):
    if numbers[0] > numbers[i]: # 7 > 3 = True
        # 자리를 바꿔준다
        temp = numbers[0]
        numbers[0] = numbers[i]
        numbers[i] = temp
    print(numbers)
