# 단순 탐색(Simple Search)
# 앞에서부터 원하는게 나올 때까지 하나하나 찾는다.
# 장점 : 만들기 쉽다, 정렬이 안되어 있어도 된다.
# 단점 : 느리다.
# 대안 : 이진탐색(Binary Search)

arr = [1,2,3,5,6,7,8,9,10,11]

# 8은 7번째, 인덱스 6번째
# 입력 받은 숫자가 몇 번째 인덱스에 있는지 찾는 함수

def simpleSearch(arr, targetNum):
    for idx in range(0, len(arr)):
        if arr[idx] == targetNum:
            return f'{arr} 의 리스트에서 {targetNum}은 {idx}번째에 위치함'
    return -1

print(simpleSearch(arr,8))
print(simpleSearch(arr,4))
