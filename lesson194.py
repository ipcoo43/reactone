# Bubble Sort
# [ 핵심 로직 ] n, n+1
# 1) 첫 번째, 두번째 비교 해서 두번째 더 작은면 첫 번째와 자리 바꿈
# 2) 

numbers = [7,3,2,9] 
print('start = [7,3,2,9]')
first = numbers[0]
second = numbers[1]
print(first, second)
temp = first
first = second
second = temp  
print(first, second)
print('[3,7,2,9]')
print()

numbers = [7,3,2,9] 
first = numbers[0]
third = numbers[2]
print(first, third)
temp = first
first = third
third = temp  
print(first, third)
print('[3,7,2,9]')
print()

numbers = [2,3,7,9]    
first = numbers[0] 
fourth = numbers[3]
print(first, fourth)
temp = first
first = fourth
fourth = temp
print(first, fourth)
print('[2,7,3,9]')