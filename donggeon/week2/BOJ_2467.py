import sys
inp = lambda : sys.stdin.readline()
N = int(inp())
fill = sorted(map(int, inp().split()))
s, e = 0, N-1
res = [fill[s], fill[e]]
while s < e:
    t = fill[s] + fill[e]
    if abs(t) < abs(res[0] + res[1]):
        res = [fill[s], fill[e]]

    if t < 0:
        s += 1
    elif t > 0:
        e -= 1
    else:
        print(fill[s], fill[e])
        exit()
print(*res)