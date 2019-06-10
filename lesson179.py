# 쉽게 설명한 삽입 정렬
# 입력 : 리스트 a
# 출력 : 정렬된 새 리스트

# 리스트 r에서 v가 들어가야 할 위치를 돌려주는 함수
def find_ins_idx(r,v):
    # 이미 정렬된 리스트 r의 자료를 앞에서부터 차례로 확인하여
    for i in range(0,len(r)):
        # v 값보다 i번 위치에 있는 자료 값이 크면
        # v가 그 값 바로 앞에 놓여야 정렬 순서가 유지됨
        if v < r[i]:
            return i
    # 절절한 위치를 못 찾았을 때는
    # v가 r의 모든 자료보다 크다는 뜻이므로 맨 뒤에 삽입
    return len(r)

def ins_sort(a):
    # 새 리스트를 만들어 정렬된 값을 저장
    result = [] 
    # 기존 리스트에 값이 남아 있는 동안 반복
    while a:
        # 기존 리스트에서 한개를 꺼냄
        value = a.pop(0)
        # 꺼낸 값이 들어갈 적당한 위치 찾기
        ins_idx = find_ins_idx(result,value)
        # 찾은 위치에 값 삽입( 이후 값은 한 칸씩 밀려남 )
        result.insert(ins_idx, value)
    return result

d = [2, 4, 5, 1, 3]

print(ins_sort(d))

# 리스트 a에 아직 자료가 남아 있다면 #  while a:
# 남은 자료 중에 맨 앞의 값을 뽑아낸다. # value=a.pop(0)
# 그 값이 result의 어느 위치에 들어가면 적당할지 알아낸다
# ins_idx=find_ins_idx(result,value)
# 위 과정에서 찾아낸 위치에 뽑아낸 값을 삽입한다
# result.insert(ins_idx, value)
# 처음 과정으로 돌아가 자료가 없을 때가지 반복한다.

# 시작
# a = [2 4 5 1 3]
# result = []

# a에서 2를 빼서 현재 비어 있는 result에 넣는다.
# a = [4 5 1 3]
# result = [2]

# a에서 4를 빼서 result의 2 뒤에 넣는다 ( 2 < 4)
# a = [5 1 3]
# result = [2 4]

# a에서 5를 빼서 result의 맨 뒤에 넣는다 (4<5)
# a = [1 3]
# result = [2 4 5]

# a에서 1를 빼서 result의 맨 앞에 넣는다 (1<2) 
# a = [3]
# result = [1 2 4 5]

# a에서 마지막 값인 3을 빼서 result의 2와 4사이에 넣는다(2<3<4)
# a=[]
# result = [ 1 2 3 4 5 ] 

# a가 비어 있으므로 종료된다.
# result의 최종결과 값이 리턴된다