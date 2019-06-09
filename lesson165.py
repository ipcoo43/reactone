def fact(n):
    if n <= 1:
        return 1
    return n*fact(n-1)
print(fact(4))

# fact(4)   # 4!
# 4*fact(3) # 4*3! 
# 3*fact(2) # 4*3*2!
# 2*fact(1) # 4*3*2*1!
# 1 ( n이 1이므로 종료 조건)
# 2 * 1     # 4*3*2
# 3 * 2 * 1 # 4*6
# 4 * 3 * 2 * 1 = 24

# def func(입력 값):
#   if 입력 값이 충분히 작으면: # 종료조건
#      return 결과값
#   func(더 작은 입력 값) # 더 작은 값으로 자기 자신을 호출
#   return 결과값
# 종료 조건이 없으면 에러 발생 한다.