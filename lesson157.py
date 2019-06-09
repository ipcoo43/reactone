# 리스트 : 정보 여러 개를 하나로 묶어 저장하고 관리 할 수 있는 기능

a = [5,7,9]
a
a[0]
a[2]
a[-1] # 끝에서 첫 번째 값, 마지막 값을 의미, n-1의미
len(a) # 리스트의 자료 개수 알수 있음

# len(a) : 리스트 길이(자료 개수) 구하기
a=[]
len(a)
len([1,2,3])

# append(x) : 자료 x를 리스트의 맨 뒤에 추가
a=[1,2,3]
a.append(4)
a
# insert(i,x) : 리스트의 i번 위치에 x를 추가
a=[1,2,3]
a.insert(0,5)
a

# pop(i) # i번 위치에 있는 자료를 리스트에서 빼내면서 그 값을 함수의 결과값으로 돌려 준다. i를 지정하지 않으면 맨 마지막 값을 빼내서 돌려 준다.
a=[1,2,3]
print(a.pop())
a

# clear() : 리스트의 모든 자료를 지운다
a=[1,2,3]
a.clear()
a

# x in a : 어떤 자료 x가 리스트 a 안에 있는지 확인
a=[1,2,3]
2 in a
5 in a
5 not in a