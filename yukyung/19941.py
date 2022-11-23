import sys
input = sys.stdin.readline
n, k = map(int, input().split()) # 식탁 길이, 햄버거 거리
arr = list(input().rstrip())

# 20 2
# HHHHHPPPPPHPHPHPHHHP
count = 0
for i in range(n):
    if arr[i] == 'P':
        for j in range(i-k, i+k+1):
            if 0 <= j < n and arr[j] == 'H':
                count += 1
                arr[j] = 'N'
                break
print(count)