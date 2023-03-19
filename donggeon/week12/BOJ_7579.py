import sys
INF = float("inf")
inp = lambda : sys.stdin.readline().split()
# 앱 i가 차지하는 메모리 -> w
# 비활성화 후 다시 활성화 시키는데 필요한 비용 -> c
## 비용을 최소화 하여 M을 확보하는데 필요한 최소한의 비용을 구하기
## M이 넘어도 비용 확보 하는거에 포함 해야함
N, M = map(int, inp())
w = list(map(int, inp()))
c = list(map(int, inp()))
cost_sum = sum(cost for cost in c)
dp = [-1 for _ in range(cost_sum + 1)]
dp[0] = 0

for memory, cost in zip(w, c):
    for i in range(cost_sum, cost - 1, -1):
        if dp[i-cost] != -1 and dp[i - cost] + memory > dp[i]:
            dp[i] = dp[i-cost] + memory

for i in range(1, cost_sum + 1):
    if dp[i] >= M:
        print(i)
        break
# # weight 담고 있음
# res = INF
# dp = [[0 for _ in range(cost_sum + 1)] for _ in range(N+1)]
# for i in range(1, N+1):
#     memory = w[i-1]
#     cost = c[i-1]
#     for j in range(1, cost_sum + 1):
#         if j < cost:
#             dp[i][j] = dp[i-1][j]
#         else:
#             # 해당 i 번째 아이템을 0-1
#             dp[i][j] = max(dp[i-1][j-cost] + memory, dp[i-1][j])
#         if dp[i][j] >= M:
#             res = min(res, j)
# print(res)