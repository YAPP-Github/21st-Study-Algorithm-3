import sys
from collections import deque
inp = lambda : sys.stdin.readline().split()
n, m = map(int, inp())
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
q = deque()
maps = []
res = [[-1] * m for _ in range(n)]
for i in range(n):
    line = list(map(int, inp()))
    maps.append(line)
    for j in range(m):
        if line[j] == 2:
            q.append((i, j))
            res[i][j] = 0
        elif not line[j]:
            # 0인 좌표는 어차피 못 가는 곳
            res[i][j] = 0
while q:
    x, y = q.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m: continue
        ## 아직 방문하지 않은 좌표
        if res[nx][ny] == -1:
            if maps[nx][ny]:
                res[nx][ny] = res[x][y] + 1
                q.append((nx, ny))
for r in res:
    print(*r)