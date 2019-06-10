# 재귀(recursive) : 자기 자신을 호출 하는 것을 말함
# 재귀함수(recursive function) : 자기 자신을 호출하는 함수
# 재귀 함수 만들기
# 탈출 조건, 끝나는 조건이 들어가야 한다

arr = [7, 3, 2, 9, 4]
def sum(arr,accu):
    #print(arr,accu)
    if(len(arr)==0):
        return accu
    return sum(arr, accu+arr.pop())

print('result =>',sum(arr,0))