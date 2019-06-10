# 재귀(recursive) : 자기 자신을 호출 하는 것을 말함
# 재귀함수(recursive function) : 자기 자신을 호출하는 함수

# 재귀 함수 만들기
# 탈출 조건, 끝나는 조건이 들어가야 한다

arr = [7, 3, 2, 9]

# recursive는 자기 자신의 상태가 변한 것을 다시 호출하는 것
def sum(arr):
    # pop() 
    # arr = [7, 3, 2, 9]
    last = arr.pop() # 9
    result = last
    
    # arr = [7, 3, 2]
    last = arr.pop() # 2
    result = result + last # 19 + 2
    
    # arr = [7, 3]
    last = arr.pop() # 3
    result = result + last
    
    # arr = [7]
    last = arr.pop() # 7
    result = result + last
    
    return result

result = sum(arr)
print('result =>',result)  # 21

# result 상태도 바뀌고 arr 상태도 바뀌는 것 : recursive