import sys
inp = lambda : sys.stdin.readline().rstrip()
N = int(inp())
balls = inp()
# B와 R 둘 중 하나만 옮길 수 있음
# B공과 R공이 각각 하나로 뭉쳐져야 함
b_count = balls.count('B')
r_count = N - b_count
# 왼쪽이나 오른쪽으로 공 한쪽으로 옮기기
res = min(b_count, r_count)
# 왼쪽으로 옮기기
cnt = 1
for i in range(1, N):
    if balls[i] != balls[0]: break
    cnt += 1
# 배열 왼쪽에서 부터 연속된 것들 빼고 R을 왼쪽으로 옮기기
if balls[0] == 'R':
    res = min(res, r_count - cnt)
else:
    res = min(res, b_count - cnt)
# 오른쪽으로 옮기기
cnt = 1
for i in range(N-2, -1, -1):
    if balls[i] != balls[-1]: break
    cnt += 1
# 배열 오른쪽에서 부터 연속된 것들 빼고 R을 오른쪽으로 옮기기
if balls[-1] == 'R':
    res = min(res, r_count - cnt)
else:
    res = min(res, b_count - cnt)
print(res)
