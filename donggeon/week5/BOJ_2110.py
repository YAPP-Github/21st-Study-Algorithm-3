import sys
inp = lambda : sys.stdin.readline()
N, C = map(int, inp().split())
house = sorted([int(inp()) for _ in range(N)])
## 3/ 1 2 4 8 9
## 1
start, end = 1, (house[-1] - house[0]) // (C - 1)
res = 0
while start <= end:
    mid = (start + end) // 2
    current = house[0]
    cnt = 1
    for h in house[1:]:
        if h >= mid + current:
            current = h
            cnt += 1
    if cnt < C:
        end = mid - 1
    else:
        res = mid
        start = mid + 1
print(res)