# 집합 : 정보를 여러 개 넣어서 보관, 중복되어 들어기지 않음, 순서도 없다

s = set()
s.add(1)
s.add(2)
s.add(2) # 중복해서 들어가지 않음
s
len(s)
{1,2} == {2,1}

# len(s) : 집합의 길이를 구한다
s = set()
len(s)
len({1,2,3})

# add(x) : 집합에 자료 x를 추가 한다.
s={1,2,3}
s.add(4)
s

# discard(x) : 집합에 자료 x가 들어 있으면 삭제 한다.
s={1,2,3}
s.discard(2)
s

# clear() : 집합의 모든 자료를 지운다
s={1,2,3}
s.clear()
s

# x in s : 어떤 자료 x가 집합 s에 들어 있는지 확인
s={1,2,3}
2 in s
5 in s
5 not in s
