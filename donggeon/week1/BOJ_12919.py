import sys
inp = lambda : sys.stdin.readline().rstrip()
S = inp()
T = inp()
def dfs(word: str):
    if word == S:
        print(1)
        exit()
    if not word: return
    if word[0] != 'B' and word[-1] != 'A': return

    # 맨 앞글자가 B이어야 B를 뺄 수 있음
    if word[0] == 'B':
        dfs(word[1:][::-1])
    # 마지막 글자가 A이어야 A를 뺄 수 있음
    if word[-1] == 'A':
        dfs(word[:-1])
dfs(T)
print(0)
# queue_s, queue_t = deque(list(S)), deque(list(T))
# # AB 에 B 붙이기 -> BBA
# def reverse_dfs():
#     if queue_s == queue_t:
#         print(1)
#         exit()
#
#     if not queue_t: return
#
#     if queue_t[0] != 'B' and queue_t[-1] != 'A':
#         return
#
#     if queue_t[0] == 'B':
#         queue_t.popleft()
#         queue_t.reverse()
#         reverse_dfs()
#         queue_t.append('B')
#         queue_t.reverse()
#     if queue_t[-1] == 'A':
#         queue_t.pop()
#         reverse_dfs()
#         queue_t.append('A')
# reverse_dfs()
# print(0)