# 1층짜리 하노이의 탑 : 원반을 한 번 이동
# 2층짜리 하노이의 탑 : 원반을 세 번 이동
# 3층짜리 하노이의 탑 : 원반을 일곱 번 이동
# 입력크기, 탑의 층수가 높을 수록 원반을 더 많이 움직여야 한다.
# 4층이면 열 다섯 번, 5층 이면 서른 한번 이동
# n층 이면 2**n-1

# 계산 복잡도
# O(1) : n과 무관하게 일정한 시간이 걸림
# O(n) : n과 비례하여 계산 시간이 증가
# O(n**2) : n의 제곱에 비례하여 계산 시간이 증가
# O(2**n) : 2의 n 제곱에 비례하여 계산 시간이 증가
# 위에서 아래로 갈수록 계산 복잡도 증가