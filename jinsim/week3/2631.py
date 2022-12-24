"""
가장 많이 연결된 숫자의 수를 찾으면 해결되는 문제이다.
"""
import sys
input = sys.stdin.readline

N = int(input())
A = []
dp = [0]*N

for _ in range(N):
    A.append(int(input()))

for i in range(N):
    for j in range(0, i):
        if A[j] < A[i] and dp[j] > dp[i]:
            dp[i] = dp[j]
    dp[i] += 1
print(N-max(dp))
