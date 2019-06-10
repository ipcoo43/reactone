# Bubble Sort
# 거품이 물에서 떠오르는 모양
# 알고리즘 공부하면 소스코드가 잘 보인다.
# 버블(거품) 정렬
# [ 핵심 로직 ]
# 첫 번째, 두번째 비교 해서 두번째 더 작은면 첫 번째와 자리 바꿈
# n, n+1

# 첫 번째, 두번째 출력
numbers = [7,3,2,9]
first = numbers[0]   # 0번째 인덱스 7
second = numbers[1]  # 1번째 인덱스 3
print(first,second)  # 7 3

# 첫 번째, 두번째 비교해서 두 번째가 더 작으면
if first > second:  # 7 > 3  = True
    # first,second = second,first  # 서로 자리를 빠꿔야 한다
    temp = first
    first = second
    second = temp
    print(first, second) # 3 7  # 자리가 바꿔 졌다.
    
