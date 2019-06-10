# 쉽게 설명한 선택 정렬
# 입력 : 리스트 a
# 출력 : 정렬된 새 리스트
# 주어진 리스트에서 최소값의 위치를 돌려주는 함수

def find_min_idx(a):
    n = len(a)
    min_idx = 0
    for i in range(1, n):
        if a[i] < a[min_idx]:
            min_idx = i
    return min_idx

def sel_sort(a):
    result = [] # 새 리스트를 만들어 정렬된 값을 저장
    while a: # 주어진 리스트에 값이 남아 있는 동안 계속
        min_idx = find_min_idx(a) # 리스트에 남아 있는 값 중 최소값의 위치
        value = a.pop(min_idx)    # 찾은 최소값을 빼내어 value에 저장
        result.append(value)      # value를 결과 리스트 끝에 추가
    return result
d = [2, 4, 5, 1, 3]
print(sel_sort(d))

# 리스트 a에 아직 자료가 남아 있다면 # while a:
# 남은 자료 중에서 최소값의 위치를 찾는다 # min_idx=find_min_idx(a)
# 찾은 최소값을 리스트 a에서 빼내어 value에 저장 # value=a.pop(min_idx)
# value를 result 리스트의 맨 끝에 추가 # result.append(value)
# 처음 과정으로 돌아가 자료가 없을 때까지 반복

# 시작            
# a = [2, 4, 5, 1, 3]
# result = []

# a 리스트의 최소값인 1을 a에서 빼내어 result에 추가한다.
# a = [ 2, 4, 5, 3]
# result = [1]

# a에 남아 있는 값 중 최소값인 2를 a에서 빼내어 result에 추가한다.
# a = [4, 5, 3]
# result = [1,2]

# a에 남아 있는 값 중 최소값인 3을 같은 방법으로 옮긴다.
# a = [4, 5]
# result = [1,2,3]

# a에 남아 있는 값 중 최소값인 4를 같은 방법으로 옮긴다.
# a = [5] 
# result = [1,2,3,4]

# a에 남아 잇는 값 중 최소값인 5를 같은 방법으로 옮긴다.
# a = []
# result = [1,2,3,4,5]

# a가 비어 있으므로 종료된다.
# result = [1,2,3,4,5] -> 최종 결과값으로 리턴된다.