import sys
inp = lambda : sys.stdin.readline().split()
N, M = map(int, inp())
# 왼쪽 대각선, 바로 아래로 내려가기, 오른쪽 대각선
## 0, 1, 2
# 같은 방향 연속 두 번 불가
maps = [list(map(int, inp())) for _ in range(N)]
# dp : 3차원 배열의 인자 값 방식으로 내려올 때 걸리는 연료
dp = [[[0, 0, 0] for _ in range(M)]] + [[[sys.maxsize for _ in range(3)] for _ in range(M)] for _ in range(N)]
for i in range(1, N+1):
    for j in range(M):
        # 마지막 열 => 왼쪽 대각선으로 내려와서 얻진 X
        if j != M-1:
            dp[i][j][0] = min(dp[i-1][j+1][1], dp[i-1][j+1][2]) + maps[i-1][j]
        # 첫 열 => 오른쪽 대각선으로 내려오지 X
        if j != 0:
            dp[i][j][2] = min(dp[i-1][j-1][0], dp[i-1][j-1][1]) + maps[i-1][j]
        dp[i][j][1] = min(dp[i-1][j][0], dp[i-1][j][2]) + maps[i-1][j]
res = sys.maxsize
for t in dp[-1]:
    res = min(min(t), res)
print(res)