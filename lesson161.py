# 중첩된 반복문
# for i in range(0, n-1)
# - i를  0부터 n-2까지 반복 한다
# - 리스트 마지막 값에 해당하는 a[n-1]은 이미 앞에서 다른 자료와 
# - 한번 다 비교했으므로 제외해도 된다.
# for j in range(i+1, n)
#  - 비교 기준으로 정해진 i번째 위치에 1을 더한 위치의 값부터 끝까지 비교

# i=0, a[i]='Tom',   j=1,2,3 : Tom, Jerry, Mike, Tom
# i=1, a[i]='Jerry', j=2,3 :  Jerry, Mike, Tom
# i=2, a[i]='Mike',  j=3 : Mike, Tom
# i=3, a[i]='Tom',       : Tom

# [ 알고리즘 분석 ] n = 4일때 비교 횟수
# 위치 | 이름  | 비교횟수 | 비교 대상
#   0  | Tom   |  3       | Jerry, Mike,Tom
#   1  | Jerry |  2       | Mike, Tom
#   2  | Mike  |  1       | Tom
#   3  | Tom   |  0       | 비교 안함
# 전체 비교 횟수 = 3 + 2 + 1 + 0 = 6

# 0번 위치 이름 : n-1번 비교
# 1번 위치 이름 : n-2번 비교
# 2번 위치 이름 : n-3번 비교
# ~
# n-2번 위치 이름 : 1번 비교
# n-1번 위치 이름 : 0번 비교
# 전체 비교 횟수 : 0+1+2+3+4+...+(n-1)번
# < 공식 >
# 1+2+3+...+(n-1) = (n-1)*(n-1+1)/2 = n*(n-1)/2, 1/2*n**2-1/2*n
# 1/2*n**2 - 1/2*n 번 비교해야 한다
# O(n**2)이라고 표현 한다
# o(n**2) : 입력 크기 n이 커지면 계산 시간은 그 제곱에 비례