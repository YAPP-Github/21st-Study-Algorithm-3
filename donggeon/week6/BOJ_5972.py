import sys, heapq
from collections import defaultdict
inp = lambda : sys.stdin.readline().split()
N, M = map(int, inp())
# 두 개 사이의 헛간 하나 이사의 길로 연결되어 있을 수 있음
# 1에서 N까지 최소 거리
distances = [sys.maxsize] * (N+1)
graph = defaultdict(list)
for _ in range(M):
    a, b, c = map(int, inp())
    graph[a].append((b, c))
    graph[b].append((a, c))
q = []
heapq.heappush(q, (0, 1))
while q:
    current_distance, current_pos = heapq.heappop(q)
    if distances[current_pos] < current_distance: continue
    for new_pos, new_distance in graph[current_pos]:
        distance = current_distance + new_distance
        if distance < distances[new_pos]:
            distances[new_pos] = distance
            heapq.heappush(q, (distance, new_pos))
print(distances[N])