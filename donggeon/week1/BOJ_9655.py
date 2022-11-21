import sys
N = int(sys.stdin.readline())
# 두 사람 게임 완벽 하게 함, 상근이가 먼저 게임
# 1, 3개 단위 마다 승자 결정하는 방식
dp = [''] * (N+3)
dp[1] = 'SK'
dp[3] = 'SK'
for i in range(2, N+1):
    if dp[i-1] == 'SK':
        if not dp[i]: dp[i] = 'CY'
        dp[i+2] = 'CY'
    else:
        if not dp[i]: dp[i] = 'SK'
        dp[i+2] = 'SK'
print(dp[N])
