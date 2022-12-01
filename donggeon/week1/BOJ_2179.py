import sys
inp = lambda : sys.stdin.readline().rstrip()
# 두 단어의 앞부분에서 공통적으로 나타나는 부분 문자열
# 앞부분에서 m개의 글자가 같고 최대인 경우
## 최대인 경우가 여러 개인 경우 앞쪽에 있는 것을 출력
words = []
### (abc, 2), (abcd, 0), (abchldp, 3), (abe, 1)
N = int(inp())
for i in range(N):
    words.append((inp(), i))
res = 0
count = [0] * N
words_origin = words.copy()
words.sort()
for i in range(N):
    temp = ''
    for j in range(min(len(words[i][0]), len(words[i-1][0]))):
        if words[i-1][0][j] == words[i][0][j]: temp += words[i][0][j]
        else: break
    t = len(temp)
    if t and t >= res:
        res = t
        count[words[i-1][1]] = max(count[words[i-1][1]], t)
        count[words[i][1]] = max(count[words[i][1]], t)
check = True
pre = ''
for i in range(N):
    if check:
        if count[i] == res:
            print(words_origin[i][0])
            pre = words_origin[i][0][:res]
            check = False
    else:
        if count[i] == res and words_origin[i][0][:res] == pre:
            print(words_origin[i][0])
            exit()