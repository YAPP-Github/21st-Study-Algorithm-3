import sys, heapq
from collections import defaultdict
inp = lambda : sys.stdin.readline().rstrip()
N = int(inp())
M = int(inp())
graph = defaultdict(dict)
for _ in range(M):
    x, y, z = map(int, inp().split())
    # 버스 정보 여러개 가능
    # 기존에 버스 정보가 있는 경우 최솟값으로 구하기
    if y in graph[x]:
        graph[x][y] = min(graph[x][y], z)
    else: graph[x][y] = z
start, end = map(int, inp().split())
distances = {i : sys.maxsize for i in range(1, N+1)}
distances[start] = 0
q = []
# 최소 힙 사용으로 가장 작은값 계속 뽑아내기
heapq.heappush(q, [distances[start], start])
while q:
    cur_distance, cur_destination = heapq.heappop(q)
    # 기존 값보다 큰 경우 continue
    if distances[cur_destination] < cur_distance: continue
    for new_destination, new_distance in graph[cur_destination].items():
        dist = cur_distance + new_distance
        if dist < distances[new_destination]:
            distances[new_destination] = dist
            heapq.heappush(q, [dist, new_destination])
print(distances[end])