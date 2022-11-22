import sys
inp = lambda : sys.stdin.readline()
N, K = map(int, inp().split())
ham = inp()
# P마다 그리디 하게 체크
## HHHHHPPPPPHPHPHPHHHP
used = [False] * N
res = 0
for i in range(N):
    if ham[i] == 'H': continue
    check = True
    start_i, end_i = i - K, i + K
    if start_i < 0: start_i = 0
    if end_i >= N: end_i = N-1
    # 왼쪽부터 찾기
    for j in range(start_i, i):
        if ham[j] == 'H' and not used[j]:
            used[j] = True
            res += 1
            check = False
            break
    if check:
        for j in range(i + 1, end_i + 1):
            if ham[j] == 'H' and not used[j]:
                used[j] = True
                res += 1
                break
print(res)
