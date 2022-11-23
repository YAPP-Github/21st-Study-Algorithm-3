# 방법 1: 짝홀수 판단
import sys
input = sys.stdin.readline
n = int(input())

if n % 2 == 0 : print('CY')
else : print('SK')

# 방법 2: DP
dp = [0]*(n+1)
dp[0] = 0
dp[1] = 1
dp[2] = 2

for i in range(3, n+1):
    dp[i] = min(dp[i-1]+1, dp[i-3]+1)

if dp[n] % 2 == 0 : print('CY')
else : print('SK')