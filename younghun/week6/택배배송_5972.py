import sys
import heapq
from collections import defaultdict

graph = defaultdict(list)
n, m = map(int, sys.stdin.readline().split())
INF = sys.maxsize

distance = [INF] * (n + 1)

for _ in range(m):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((v, w))
    graph[v].append((u, w))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)  # 현재까지 거리를 구한 노드 중 최단거리 노드 선택.

        if distance[now] < dist:  # 이미 구해진 거리가 더 작다면 이미 방문해서 최단거리를 구한 노드.
            continue

        for node, weight in graph[now]:  # 연결된 모든 노드 탐색
            if dist + weight < distance[node]:  # 해당 노드를 거쳐가는 거리가 더 작다면
                distance[node] = dist + weight  # 최단거리 갱신
                heapq.heappush(q, (dist + weight, node))  # 새롭게 갱신한 노드 우선순위 큐에 추가.


dijkstra(1)
print(distance[n])
