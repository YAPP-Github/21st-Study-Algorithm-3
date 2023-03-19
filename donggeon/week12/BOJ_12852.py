import sys
N = int(sys.stdin.readline())
# 3으로 나누어 떨어지면 3으로 나누기
# 2로 나누어 떨어지면 2로 나누기
# 1빼기
## 1 만들기
## 연산 회수랑 연산 출력
dp = {1: (0, [1])}
def op(x):
    if x in dp.keys():
        return dp[x]
    if not x % 3 and not x % 2:
        tmp1 = op(x // 3)
        tmp2 = op(x // 2)
        if tmp1[0] < tmp2[0]:
            dp[x] = (tmp1[0] + 1, tmp1[1] + [x])
        else:
            dp[x] = (tmp2[0] + 1, tmp2[1] + [x])
    elif not x % 3:
        tmp1 = op(x // 3)
        tmp2 = op(x - 1)
        if tmp1[0] < tmp2[0]:
            dp[x] = (tmp1[0] + 1, tmp1[1] + [x])
        else:
            dp[x] = (tmp2[0] + 1, tmp2[1] + [x])
    elif not x % 2:
        tmp1 = op(x // 2)
        tmp2 = op(x - 1)
        if tmp1[0] < tmp2[0]:
            dp[x] = (tmp1[0] + 1, tmp1[1] + [x])
        else:
            dp[x] = (tmp2[0] + 1, tmp2[1] + [x])
    else:
        tmp = op(x - 1)
        dp[x] = (tmp[0] + 1, tmp[1] + [x])
    return dp[x]
res = op(N)
print(res[0])
print(*res[1][::-1])
# res = [N]
# q = deque([[0, [N]]])
# visited = [False] * (N + 1)
# while q:
#     cnt, path = q.popleft()
#     t = path[-1]
#     visited[t] = True
#     if t == 1:
#         print(cnt)
#         print(*path)
#         break
#     if not t % 3:
#         if not visited[t // 3]:
#             q.append((cnt + 1, path + [t // 3]))
#     if not t % 2:
#         if not visited[t // 2]:
#             q.append((cnt + 1, path + [t // 2]))
#     if not visited[t - 1]:
#         q.append((cnt + 1, path + [t - 1]))