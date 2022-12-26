import sys
import heapq

# 초기 선언
input = sys.stdin.readline
INF = sys.maxsize

N, M = map(int, input().split())
# 각 노드에 도착한 시각을 저장하는 리스트
times = [INF for _ in range(N+1)]
times[1] = 0

# 노드 별로 다음 위치와 시간을 넣을 이중 리스트
graph = [[] for _ in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    graph[0].append((i, b))
    graph[1].append((i, a))

# 힙 생성 (시간, 노드)
Q = [(0, 1)]

while Q:
    t, n = heapq.heappop(Q)
# 도착한 경우
    if n == N:
        print(t)
        break
	# 도착 가능한 노드에 대한 시간을 계산한다.
    for dest_t, dest_n in graph[n]:
	# t d m
	# d가 크고, m이 그 이상인 경우
	# 1 5 10
	# t가 크고, m이 그 이상인 경우
	# 15 2 19
	# t가 크고, m이 그 사이인 경우
	# 15 2 4
	# 한 주기에 여러번 들어와도 괜찮은 이유
	# 2 9 10 7
	# 2 1 10 9
	# dest_t와 t 의 차이에서 주기에 대한 나머지를 구하면 그것이 현재 시간 기준에서 기다려야하는 시간이다.
	# 거기에 현재까지 시간과 횡단보도 건너는 시간 1을 더해준다.
        total_t = (dest_t - t) % M + t + 1
        if total_t < times[dest_n]:
            times[dest_n] = total_t
            heapq.heappush(Q, (total_t, dest_n))
