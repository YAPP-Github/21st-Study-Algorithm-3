import sys
inp = lambda : sys.stdin.readline().rstrip()
N = int(inp())
origin = list(map(int, inp()))
target = list(map(int, inp()))
origin_copy = origin[:]
# i 번 스위치 누르면 i-1, i, i+1 전구 상태 변경
# 첫 번째 스위치 누르면 1, 2번째 전구 상태 변경
# N 번째 스위치 누르면 N-1, N번째 전구 변경
## 최소 몇 번 -> 그리디 알고리즘 적용
cnt = 0
for k in range(2):
    temp = origin if not k else origin_copy
    cnt = 0
    if not k and temp != target:
        for j in range(2):
            temp[j] = 1 - temp[j]
        cnt += 1

    for i in range(1, N):
        if i == N-1:
            if temp[i-1] != target[i-1]:
                for j in range(N-2, N):
                    temp[j] = 1- temp[j]
                cnt += 1
        else:
            if temp[i-1] != target[i-1]:
                for j in range(i-1, i+2):
                    temp[j] = 1 - temp[j]
                cnt += 1
    ## 매번 비교 하면 O(N) 연산 매번 일어남. 차라리 한 번 하는게 나음
    if temp == target:
        print(cnt)
        exit()
print(-1)