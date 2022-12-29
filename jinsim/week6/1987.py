# BFS, 덱을 이용한 풀이
import sys
from collections import deque
input = sys.stdin.readline

move = [[1, 0], [-1, 0], [0, 1], [0, -1]]
R, C = map(int, input().split())
# rstrip 보다 빠름
board = [input().strip('\n') for _ in range(R)]
# 탐색 도중 겹치는 경로를 제거하기 위함.
visited = [["" for _ in range(C)] for _ in range(R)]

Q = deque()
Q.append((0, 0, board[0][0]))
while Q:
    y, x, v = Q.popleft()
    # 선입선출에 BFS이므로, 마지막에 남아있는 경로가 제일 긴 경로이다.
    ret = v
    for dy, dx in move:
        ny = dy + y
        nx = dx + x
        if 0 <= ny < R and 0 <= nx < C and board[ny][nx] not in v:
            n = v+board[ny][nx]
            # 만약 해당 노드를 같은 경로로 방문했다면 큐에 추가하지 않는다.
            if visited[ny][nx] != n:
                visited[ny][nx] = n
                Q.append((ny, nx, n))
print(len(ret))
