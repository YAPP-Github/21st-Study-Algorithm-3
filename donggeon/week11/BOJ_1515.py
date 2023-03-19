import sys
nums = list(map(int, sys.stdin.readline().rstrip()))
# 직전 수 보다 큰 수가 나오게 최소로 그리디 하게 탐색
## 234092 -> 20
i, N = 0, 0
while i < len(nums):
    N += 1
    ## 다음 숫자 길이에 따라 index 판단
    temp = [int(k) for k in str(N)]
    for j in range(len(temp)):
        if i == len(nums): break
        if nums[i] == temp[j]:
            i += 1
print(N)