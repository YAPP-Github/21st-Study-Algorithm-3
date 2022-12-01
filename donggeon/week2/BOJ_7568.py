import sys
inp = lambda : sys.stdin.readline()
# (x, y), (p, q) < 키, 몸무게> x >y 이고 p > q -> 덩치 더 크다
N = int(inp())
body = [list(map(int, inp().split())) for i in range(N)]
rank = [1 for j in range(N)]
for i in range(N):
    for j in range(N):
        if body[i][0] < body[j][0] and body[i][1] < body[j][1]:
            rank[i] += 1
print(*rank)