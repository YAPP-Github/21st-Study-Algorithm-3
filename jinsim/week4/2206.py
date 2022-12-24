import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

# 미로 생성
miro = [input().rstrip("\n") for _ in range(N)]

# 이동 가능
move = ((0, 1), (0, -1), (1, 0), (-1, 0))

# 우선순위큐 생성. 다만 가중치가 동일하므로 heap을 쓰지 않아도 된다.
Q = deque()
# y좌표, x좌표, 벽을 부수고 왔는지 (0 or 1)
Q.append((0, 0, 0))

# 0으로 초기화하고, 가중치의 누적 합을 저장한다.
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
visited[0][0][0] = 1

# 도착 못한 경우 -1을 반환한다.
ret = -1

while Q:
    y, x, b = Q.popleft()

# 0 부터 구성되었으므로 1씩 뺀 좌표에 도착했을 때가 답이다.
    if y == N-1 and x == M-1:
        ret = visited[y][x][b]
        break

	# 갈 수 있는 좌표 체크
    for dy, dx in move:
        ny = dy + y
        nx = dx + x
	# 미로를 벗어나거나, 이미 도착한 좌표인 경우는 제외한다.
        if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx][b]:

		# 도착 예상 지점이 뚫려있는 경우는 그냥 넣어준다.
            if miro[ny][nx] == '0':
                Q.append((ny, nx, b))
                visited[ny][nx][b] = visited[y][x][b] + 1

		# 도착 예상 지점이 막혀있는 경우는, 현재까지 부순 적이 없을 때만 넣어준다.
            elif b == 0:
                Q.append((ny, nx, 1))
                visited[ny][nx][1] = visited[y][x][0] + 1

print(ret)
