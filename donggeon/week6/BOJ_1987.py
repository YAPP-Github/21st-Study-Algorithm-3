import sys
inp = lambda : sys.stdin.readline().rstrip()
R, C = map(int, inp().split())
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
boards = []
for _ in range(R):
    boards.append(list(inp()))
res = 1
# 중복 방지를 위한 set
q = set([(0, 0, boards[0][0])])
while q:
    x, y, path = q.pop()
    res = max(res, len(path))
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < R and 0 <= ny < C and boards[nx][ny] not in path:
            q.add((nx, ny, boards[nx][ny] + path))
print(res)