import sys
inp = lambda : sys.stdin.readline().split()
# L * L 크기의 트램펄린 -> 최대한 많은 별똥별 우주로 튕겨내기
N, M, L, K = map(int, inp())
# 단순 리스트를 만들면 너무 큰 리스트 => 메모리 초과
stars = [list(map(int, inp())) for _ in range(K)]
res = 0
def count(x, y):
    cnt = 0
    for k in range(K):
        # x + L까지 포함
        if x <= stars[k][0] <= x + L and y <= stars[k][1] <= y + L:
            cnt += 1
    return cnt
# 사분면 느낌
for i in range(K):
    for j in range(K):
        res = max(res, count(stars[i][0], stars[j][1]))
print(K - res)