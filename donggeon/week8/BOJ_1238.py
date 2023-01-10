import sys, heapq
from collections import defaultdict
inp = lambda : sys.stdin.readline().split()
N, M, X = map(int, inp())
graph = defaultdict(dict)
graph_r = defaultdict(dict)
distances = [sys.maxsize] * (N+1)
distances_r = [sys.maxsize] * (N+1)
# 도로는 단방향, 중복 X
for _ in range(M):
    a, b, c = map(int, inp())
    graph[a][b] = c
    graph_r[b][a] = c
def dijkstra(d: list, g: defaultdict):
    q = []
    heapq.heappush(q, (0, X))
    while q:
        cur_distance, cur_pos = heapq.heappop(q)
        if cur_distance > d[cur_pos]: continue
        for next_pos, next_distance in g[cur_pos].items():
            distance = cur_distance + next_distance
            if distance < d[next_pos]:
                d[next_pos] = distance
                heapq.heappush(q, (distance, next_pos))
dijkstra(distances, graph)
dijkstra(distances_r, graph_r)
res = 0
for i in range(1, N+1):
    if i != X:
        res = max(res, distances[i] + distances_r[i])
print(res)