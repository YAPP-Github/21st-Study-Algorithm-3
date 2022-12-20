import sys
inp = lambda : sys.stdin.readline()
N, d, k, c = list(map(int, inp().split()))
arr = [int(inp()) for _ in range(N)]
food = [0] * (d + 1)
cnt = 1
food[c] += 1
for i in range(k):
    if food[arr[i]] == 0:
        cnt += 1
    food[arr[i]] += 1
ans = cnt
for i in range(1, N):
    if food[arr[(i - 1) % N]] == 1:
        cnt -= 1
    food[arr[(i - 1) % N]] -= 1
    if not food[arr[(i + k - 1) % N]]:
        cnt += 1
    food[arr[(i + k - 1) % N]] += 1
    ans = max(ans, cnt)
print(ans)
