# 가장 많이 등장하는 알파벳의 개수 구하기
# ex) mouse : 1, test :2, hello :2

word = 'test'

def highFrequencyLetterCount(word):
    map = {}
    for alphabet in word:
        if map.get(alphabet) == None:
            map[alphabet] = 1
        else:
            map[alphabet] += 1
        print('map : ',map)

    return -1

print(highFrequencyLetterCount(word))