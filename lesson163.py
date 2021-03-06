# 러시아 인형 : 마트료시카
# - 큰 인형을 열면 그 안에 비슷하게 생긴 작은 인형
# - 또 그 안에 조금 더 작은 인형이 있다.
# - 이 처럼 인형이 계속 반복되어 나오다가 더 작게 만들기 힘들 정도 작은인형
# 러시아 인형의 특징
# - 인형 안에는 자기 자신과 똑같이 생긴, 크기만 약간 작은 인형이 들어 있음
# - 인형 안에서 작은 인형이 반복되어 나오다가 인형을 더 작게 만들기 힘들면
# - 마지막 인형이 나오면서 반복이 끝납니다.
# - 마지막 인형 안에 사탕이 들어 있음
# 재귀호출(recursiont) : 언떤 함수 안에서 자기 자신을 부르는 것

def hello():
    print('hello')
    #hello() # hello() 함수 안에서 다시 hello()를 호출
hello() # hello() 함수 호출

# 무한 반복이 된다.으로 에러 발생하는 재귀 호출은 아니고
# 재귀 호출의 개념 이해를 위한 것이다
# 재귀 호출을 정상적으로 작동하려면 '종료 조건'이 필요하다.
# 특정 조건이 되면 더 자신을 호출하지 않고 멈추도록 설계가 필요한다.
# 재귀 호출 함수가 계산 결과를 돌려 줄 때 return 명령을 사용해서
# 종료 조건의 결과값부터 돌려줍니다.
