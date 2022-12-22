import sys
import heapq
# 입력이 많으므로 input을 최적화해준다.
input = sys.stdin.readline

N = int(input())
M = int(input())

# 그래프 인접 리스트 생성.
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
# N(1000)에 비해 M(100000)이 훨씬 크므로, 같은 출발지와 도착지를 가진 버스가 여러 개인 경우를 고려해야 한다.
# 비용을 기준으로 정렬해준다.
for i in range(N+1):
    graph[i].sort(key=lambda x: x[1])

start, end = map(int, input().split())

# 출발 정점으로부터 비용. 최대값으로 생성해둔다.
distances = [sys.maxsize] * (N+1)
# 초기 정점을 0으로 설정한다.
distances[start] = 0

# 힙 생성(비용, 정점)
Q = [(0, start)]

# 다익스트라 알고리즘
while Q:
    dist, node = heapq.heappop(Q)
    # 이미 들린 비용이 더 적은 은 경우, 다음으로 넘어간다.
    if dist > distances[node]:
        continue
    # 각 정점에서 들릴 수 있는 정점 중, 현재까지의 비용보다 더 적게 갈 수 있는 것만 채택한다.
    for dest_node, dest_dist in graph[node]:
        new_dist = dist + dest_dist
        # 비용을 갱신하고, 힙에 추가한다.
        if new_dist < distances[dest_node]:
            distances[dest_node] = new_dist
            heapq.heappush(Q, (new_dist, dest_node))

print(distances[end])
