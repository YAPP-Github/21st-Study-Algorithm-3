import sys
from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
inp = lambda : sys.stdin.readline().rstrip()
R, C = map(int, inp().split())
maps = []
q, fire_q = deque(), deque()
for i in range(R):
    line = list(inp())
    for j in range(C):
        if line[j] == 'J':
            q.append((i, j))
        elif line[j] == 'F':
            fire_q.append((i, j))
    maps.append(line)
time = 0
while True:
    time += 1
    temp = []
    while fire_q:
        x, y = fire_q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if -1 < nx < R and -1 < ny < C and maps[nx][ny] != '#' and maps[nx][ny] != 'F':
                temp.append((nx, ny))
                maps[nx][ny] = 'F'
    fire_q = deque(temp)
    temp = []
    while q:
        x, y = q.popleft()
        if x == 0 or x == R - 1 or y == 0 or y == C - 1:
            print(time)
            exit()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if -1 < nx < R and -1 < ny < C and maps[nx][ny] == '.':
                temp.append((nx, ny))
                maps[nx][ny] = 'V'
    q = deque(temp)
    if not q: break
print('IMPOSSIBLE')