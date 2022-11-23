import sys
from collections import deque
N, K = map(int, sys.stdin.readline().split())
q = deque([N])
pos_max = 100000
# 방문 여부 체크용
count = [-1] * (pos_max + 1)
count[N] = 0
while q:
    p = q.popleft()
    if p * 2 <= pos_max and count[p * 2] == -1:
        q.appendleft(p * 2)
        count[p * 2] = count[p]
    for i in (p-1, p+1):
        if 0 <= i <= pos_max and count[i] == -1:
            q.append(i)
            count[i] = count[p] + 1
print(count[K])