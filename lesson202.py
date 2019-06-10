# 가장 많이 등장하는 알파벳의 개수 구하기
# ex) mouse : 1, test :2, hello :2

word = 'elegance'

def highFrequencyLetterCount(word):
    map = {}
    for alphabet in word:
        if map.get(alphabet) == None:
            map[alphabet] = 1
        else:
            map[alphabet] += 1
        # print('map : ',map)
    
    max = -1
    for key in map:
        # print('key :',key, 'value :',map[key],'max :',max)
        if map[key] > max:
            max = map[key]

    return max

print('result :',highFrequencyLetterCount(word))