import sys
from collections import deque
input = sys.stdin.readline

# 이동을 위한 리스트
move = [[1,0],[-1,0],[0,1],[0,-1]]
n, m = map(int, input().split())
# 결과값으로 둘 이중 리스트. 모든 땅을 -1로 초기화
ret=[[-1 for _ in range(m)] for _ in range(n)]

# 출발지를 찾기 위한 변수
find = False
# 땅들을 저장할 이중 리스트
board = []
for i in range(n):
    lands = list(map(int,input().split()))
    # 각 땅들을 다 탐색
    for j in range(m):
        # 아직 출발지를 못 찾은 경우에는, 2인지 확인 후 맞다면 출발 좌표로 지정
        if not find and lands[j] == 2:
            s_y = i
            s_x = j
            find = True
        # 0으로 된 땅은 결과값 리스트의 해당 좌표를 -1에서 0으로 변경
        if not lands[j]:
            ret[i][j] = 0
    board.append(lands)

# 큐를 만들고, 출발좌표 지정.
Q = deque()
Q.append((s_y, s_x))
ret[s_y][s_x] = 0

# BFS 시작
while Q:
    y, x = Q.popleft()
    for dy, dx in move:
        ny = dy + y
        nx = dx + x
        # 갈 수 있는 땅인 경우
        if 0 <= ny < n and 0 <= nx < m and board[ny][nx]:
            # 아직 도착하지 못했고, 출발지가 아닌 경우
            if ret[ny][nx] == -1 and not (ny == s_y and nx == s_x):
                ret[ny][nx] = ret[y][x]+1
                Q.append((ny, nx))

for i in range(n):
    print(*ret[i])