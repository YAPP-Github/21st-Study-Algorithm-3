import sys
inp = lambda : sys.stdin.readline()
N = int(inp())
A = sorted(map(int, inp().split()))
res = 0
def two_pointer(arr, target):
    global res
    start, end = 0, len(arr) - 1
    while start < end:
        temp = arr[start] + arr[end]
        if temp == target:
            res += 1
            break
        elif temp < target:
            start += 1
        else:
            end -= 1
# 나머지 수 중 두 개의 수의 합 이므로 세번째 수 부터 돌 수 있음
if N < 3:
    res = 0
else:
    for i in range(N):
        # 자기 자신 제외하고 두 수 구하기
        two_pointer(A[:i] + A[i+1:], A[i])
    print(res)

# for i in range(N):
#     start, end = 0, N - 1
#     check = False
#     # 서로 다른 두 수
#     while start < end:
#         # start나 end가 i인 경우 skip
#         if start == i:
#             start += 1
#         if end == i:
#             end -= 1
#         if start >= end: break
#
#         temp = A[start] + A[end]
#         if temp == A[i]:
#             check = True
#             break
#         elif temp < A[i]:
#             start += 1
#         else:
#             end -= 1
#     if check: res += 1
