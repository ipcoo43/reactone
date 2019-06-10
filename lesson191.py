# 퀵 정렬
# 정렬 : 버블, 선택, 삽입, 병합, 퀵
# 퀵정렬 : 가장 빠른 정렬
# 나눠서 정렬
# [40,35,27,50,75] 
# 40으로 -> 35 40 -> 27 35 40 -> 40,35,27,50,75
# 기준을 선택한 후 양쪽에 큰수 작은수 배열
# 재귀를 이용해서 남은 원소를 계속 함수를 태움

numbers = [40, 35, 27, 75, 50]

def quickSort(array):
    if len(array) < 2: # 원소 크기가 한 개일 때 (2보다 작으면)
        return array   # 원소를 리턴 한다
    else:
        pivot = array[0] # 기준을 0번으로 정한후
        # less = array[1:] # 1번부터 끝까지
        # 1번 부터 끝까지 원소들 중 기준(pivot) 보다 작거나 같은것)
        less = [number for number in array[1:] if number <= pivot ]
        # 1번 부터 끝까지 원소들 중 기준(pivot) 보다 큰것)
        greater = [number for number in array[1:] if number > pivot ]
        print('less:',less)
        print('greater:',greater)
        return quickSort(less) + [pivot] + quickSort(greater)

result = quickSort(numbers)
print(result)