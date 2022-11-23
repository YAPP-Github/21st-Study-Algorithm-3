from collections import deque
import sys

input = sys.stdin.readline
# n 수빈, k 동생
n, k = map(int, input().split())
q = deque()
q.append(n)

visited = [0 for _ in range(100001)]
visited[n] = 0

while q:
    s = q.popleft()
    if s == k:
        print(visited[s])
        break
    if 0 <= s-1 < 100001 and visited[s-1] == 0:
        visited[s-1] = visited[s] + 1
        q.append(s-1)
    if 0 < s*2 < 100001 and visited[s*2] == 0:
        visited[s*2] = visited[s]
        q.appendleft(s*2)
    if 0 <= s+1 < 100001 and visited[s+1] == 0:
        visited[s+1] = visited[s] + 1
        q.append(s+1)