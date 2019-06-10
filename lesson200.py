# StringTokenizer 만들기
# 토큰(Token) : 프로그램에서 다루는 최소 단위
# 예) 이름 홍길동을 다룰 때 홍은 성이고, 길동은 이름이다. 
#     이 각각을 토큰이라고 한다.
# Tokenizer : 가장 작은 단위로 나누어 주는 일을 하는테 토크나이저.
# 왜 나누느냐 : 나눠서 처리 해야 하기 때문
# StringTokeninzer란 : 스트링을 나누어 주는 로직이 스트링 토크나이저 이다.
# string = '1+2*(3-4)'
# first = 3-4      # -1
# second = 2*(-1)  # -2
# third = 1+(-2)   # -1
# 1 + (2 * 3) - ( 2 * 4)
# 1 + (6) - (8)
# 7 - 8
# -1
# 숫자와 괄호를 분리 해주는 식

string = '13+3*{24*(35-46.76)-89}'   # 13+24*(35-46.76)
def stringTokenizer(string, deli):
    result = []
    accu = ""
    for chr in string:
        if chr in deli:
            if accu != "":
                result.append(accu)
                accu = ""
            result.append(chr)
        else:
            accu = accu + chr

    return result

print('result =>',stringTokenizer(string,"+-*/()[]{}^"))