import sys

input=sys.stdin.readline
n,k=map(int,input().split())
loc=list(input())
people=0
for i in range(n):
    if loc[i]=='P':
        for j in range(i-k,i+k+1):
            if 0<=j<n and loc[j]=='H':
                people+=1
                loc[j]=None
                break

print(people)
