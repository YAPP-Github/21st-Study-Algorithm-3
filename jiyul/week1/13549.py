from collections import deque
import sys

input=sys.stdin.readline
n,k = map(int,input().split())

def bfs():
    visited = [-1]*100001
    visited[n]=0
    queue=deque([n])

    while queue:
        cur=queue.popleft()

        if cur==k:
            return visited[cur]

        for nxt in (cur+1,cur-1,cur*2):

            if 0<=nxt<=100000 and visited[nxt]==-1:
                if nxt == cur*2:
                    visited[nxt]= visited[cur]
                    queue.appendleft(nxt)
                else:
                    visited[nxt]=visited[cur]+1
                    queue.append(nxt)

print(bfs())