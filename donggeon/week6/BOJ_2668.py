import sys
inp = lambda : int(sys.stdin.readline())
# 집합이 일치해야 함
# 일치하는 집합 중 최대인 경우
# 자기 자신과 같은 경우는 모두 포함 되어야 최대
## 1 2 3 4 5 6 7
## 3 1 1 5 5 4 6
N = inp()
nums = [0] + [inp() for _ in range(N)]
min_set = {i for i in range(1, N+1) if i == nums[i]}
res_set = set()
visited = [False] * (N+1)
for i in min_set:
    visited[i] = True
for i in range(1, N+1):
    stack = [i]
    temp_set = min_set.copy()
    index_set = min_set.copy()
    while stack:
        t = stack.pop()
        if not visited[nums[t]]:
            visited[nums[t]] = True
            index_set.add(t)
            temp_set.add(nums[t])
            stack.append(nums[t])
    if index_set == temp_set:
        for t in temp_set:
            res_set.add(t)
    else:
        for t in temp_set:
            visited[t] = False
print(len(res_set))
for r in sorted(res_set):
    print(r)