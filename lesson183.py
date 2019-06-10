# 쉽게 설명한 병합 정렬
# 입력 : 리스트 a
# 출력 : 정렬된 새 리스트

def merge_sort(a):
    n = len(a)
    # 종료 조건 : 정렬할 리스트의 자료 개수가 한 개 이하이면 정렬할 필요 없음
    if n <= 1:
        return a
    # 그룹을 나누어 각각 병합 정렬을 호출하는 과정
    mid = n // 2  # 중간을 기준으로 두 그룹으로 나눔
    g1 = merge_sort(a[:mid]) # 재귀 호출로 첫 번째 그룹을 정렬
    g2 = merge_sort(a[mid:]) # 재귀 호출로 두 번째 그룹을 정렬
    # 두 그룹을 하나로 병합
    result = [] # 두 그룹을 합쳐 만들 최종 결과
    while g1 and g2: # 두 그룹에 모두 자료가 남아 있는 동안 반복
        if g1[0] < g2[0]: # 두 그룹의 맨 앞 자료 값을 비교 g1 값이 더 작으면
            result.append(g1.pop(0)) # 그 값을 빼내어 결과로 추가 한다
        else:  # g2 값이 더 작으면
            result.append(g2.pop(0)) # 그 값을 빼내어 결과로 추가 한다.
    # 아직 남아 있는 자료들을 결과에 추가
    # g1과 g2중 이미 빈 것은 while을 바로 지나감
    while g1:
        result.append(g1.pop(0))
    while g2:
        result.append(g2.pop(0))
    return result

d = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]

print(merge_sort(d))

# 종료 조건
# n = len(a)
# if n <= 1:
#    return a
# 입력으로 주어진 리스트 a의 크기가 1이하이면
# 자료가 한 개뿐이거 아예 비어 있다면
# 절렬한 필요가 없으므로 입력 리스트를 그대로 돌려주면서 재귀 호출 종료

# 전체 리스트를 절반으로 나눠 각각 재귀 호출로 병합 정렬
# mid = n // 2  # 두 그룹으로 나누기 위한 중간 값
# g1 = merge_sort(a[:mid]) # 재귀 호출로 첫 번째 그룹 정렬
# g2 = merge_sort(a[mid:]) # 재귀 호출로 두 번째 그룹 정렬

# 리스트 자료 개수가 홀수 일때
# n // 2 -> n을 2로 나눈 몫이므로 n이 5인 홀수인 경우 
# 5 // 2 -> 2가 된다.
# 자료가 두 개인 그룹과 세 개인 그룹으로 나눈다
# a[:mid] -> 리스트 a의 0번 위치부터 mid위치 진전까지
# a[mid:] -> 리스트 a의 mid 위치부터 끝까지 

a = [1,2,3,4,5]
mid = len(a) // 2
print(mid)
print(a[:mid])
print(a[mid:])
