import sys
inp = lambda : sys.stdin.readline().split()
# 1층부터 N층까지 엘베 사용
# 엘베 최대 K 자리수
# LED 최대 P개 반전
# 실제로 X층에 멈춰있음
## 각각 led로 표현?
led = dict()
led[0] = [[1, 0], [1, 1], [0, 0], [1, 1], [1, 0]]
led[1] = [[0, 0], [0, 1], [0, 0], [0, 1], [0, 0]]
led[2] = [[1, 0], [0, 1], [1, 0], [1, 0], [1, 0]]
led[3] = [[1, 0], [0, 1], [1, 0], [0, 1], [1, 0]]
led[4] = [[0, 0], [1, 1], [1, 0], [0, 1], [0, 0]]
led[5] = [[1, 0], [1, 0], [1, 0], [0, 1], [1, 0]]
led[6] = [[1, 0], [1, 0], [1, 0], [1, 1], [1, 0]]
led[7] = [[1, 0], [0, 1], [0, 0], [0, 1], [0, 0]]
led[8] = [[1, 0], [1, 1], [1, 0], [1, 1], [1, 0]]
led[9] = [[1, 0], [1, 1], [1, 0], [0, 1], [1, 0]]
N, K, P, X = map(int, inp())
compare = [] * K
comparator = 10 ** (K-1)
t = X
while comparator:
    q = t // comparator
    t = t % comparator
    comparator = comparator // 10
    compare.append(led[q])
res = 0
for i in range(1, N + 1):
    if i == X: continue
    temp = []
    comparator = 10 ** (K - 1)
    num = i
    while comparator:
        q = num // comparator
        num = num % comparator
        comparator = comparator // 10
        temp.append(led[q])
    cnt = 0
    for j in range(K):
        for k in range(5):
            for l in range(2):
                if temp[j][k][l] != compare[j][k][l]: cnt += 1
    if cnt <= P:
        res += 1
print(res)