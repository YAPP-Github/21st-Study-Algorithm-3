import sys

input=sys.stdin.readline
n=int(input())

DP=[-1]*1001
DP[0]=0
DP[1]=1
DP[2]=2

for i in range(3,n+1):
    DP[i]=min(DP[i-3]+1,DP[i-1]+1)

if(DP[n]%2==1):
    print("SK")
else:
    print("CY")