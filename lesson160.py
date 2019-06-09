# 동명이인 찾기
# n명의 사람 이름 중에서 같은 이름을 찾아 집합으로 만들어 돌려주는 주기
# 입력 : n명의 이름이 들어 있는 리스트
# 출력 : 같은 이름들이 들어 있는 집합(set)
# 자료 : ['Tom','Jerry','Mike','Tom']
# < 생각 >
# - Tom을 뒤에 있는 'Jerry','Mike','Tom'과 차례로 비교한다
# - Tom과 마지막 Tom이 같으므로 동명이인이 된다.
# - 두 번째 Jerry를 뒤에 있는 'Mike','Tom'과 비교 한다
# - 세 번째 Mike를 뒤에 있는 Tom과 비교 한다
# - 마지막 Tom은 비교하지 않아도 된다.
# - 같은 이름은 Tom 하나 뿐이다.
# < 주의할 점 >
# - 비교할 이름을 뽑은 다음에는 뽑은 이름보다 뒤에 있는 이름과 비교
# - 마지막 이름을 기준으로 비교 하지 않아도 된다.
# - 같은 이름을 찾으면 결과 집합에 그 이름 추가 한다.

def find_same_name(a):
    n = len(a) # 리스트의 자료 개수를 n에 저장
    result = set() # 결과를 저장할 빈 집합
    for i in range(0, n-1): # 0부터 n-1까지 반복
        for j in range(i+1,n): # i+1부터 n까지 반복
            if a[i] == a[j]:  # 이름이 같으면
                result.add(a[i]) # 찾은 이름을 result에 추가
    return result

name = ['Tom', 'Jerry', 'Mike', 'Tom']
print(find_same_name(name))

name2 = ['Tom', 'Jerry', 'Mike', 'Tom', 'Mike']
print(find_same_name(name2))