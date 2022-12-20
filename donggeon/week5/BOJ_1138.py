import sys
inp = lambda : sys.stdin.readline().rstrip()
N = int(inp())
# 자기보다 큰 사람 몇 명 이었는지 기억 정보
## 키 작은 사람부터 자기 왼쪽에 큰 사람 몇 명 있었는지
watch = list(map(int, inp().split()))
# 키 큰 사람부터 insert 시키기 위해
watch.reverse()
## 4
## 2 1 1 0
stand = []
for i in range(N):
    # insert(i, x) : i 위치에 x 추가
    stand.insert(watch[i], N-i)
print(*stand)

# 순열을 사용한 풀이 : 풀리긴 하나 시간 오래걸림
# stand_perm = permutations([i+1 for i in range(N)], N)
# for s in stand_perm:
#     s_list = list(s)
#     check = True
#     for i in range(len(s_list)):
#         count = 0
#         for j in range(i):
#             if s_list[j] > s_list[i]: count += 1
#         if count != watch[s_list[i]-1]:
#             check = False
#             break
#     if check:
#         print(*s_list)