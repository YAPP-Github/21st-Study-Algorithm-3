import sys, heapq
from collections import defaultdict
inp = lambda : sys.stdin.readline().split()
N, M = map(int, inp())
crossroads = defaultdict(list)
for i in range(M):
    start, end = map(int, inp())
    crossroads[start].append((end, i))
    crossroads[end].append((start, i))
distances = [sys.maxsize] * (N+1)
distances[1] = 0
queue = []
heapq.heappush(queue, (distances[1], 1))
while queue:
    cur_time, cur_node = heapq.heappop(queue)
    if cur_node == N:
        break
    if distances[cur_node] < cur_time:
        continue
    for new_node, new_time in crossroads[cur_node]:
        time = new_time + ((cur_time - new_time) // M) * M if (cur_time - new_time) % M == 0 else new_time + ((cur_time - new_time) // M + 1) * M
        if distances[new_node] > time + 1:
            distances[new_node] = time + 1
            heapq.heappush(queue, (distances[new_node], new_node))
print(distances[N])
## 1 2
## 3 4
## 1 3
## 4 1
## 2 3

# 0에서 부터 출발 했을 때 최솟값
# dp = [sys.maxsize] * (N+1)
# dp[1] = 0
# time = 0
# while True:
#     # crossroads 배열의 출발지 값 가지고 비교
#     start, end = crossroads[time % M][0], crossroads[time % M][1]
#     if dp[start] != sys.maxsize:
#         dp[end] = min(dp[end], time + 1)
#     if dp[end] != sys.maxsize:
#         dp[start] = min(dp[start], time + 1)
#
#     if dp[N] != sys.maxsize:
#         print(dp[N])
#         break
#     time += 1