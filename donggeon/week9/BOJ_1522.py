import sys
inp = lambda : sys.stdin.readline().rstrip()
# a를 모두 연속으로 만들기
# 연속임을 판별하는 조건
words = inp()
N = len(words)
# a의 개수를 구하고 그만큼 구간을 만들어 한 칸 씩 이동하여 b의 개수 세기
# 가장 적은 b의 개수 출력
a_cnt = words.count('a')
left = 0
res = sys.maxsize
while left < N:
    right = left + a_cnt
    if right > len(words):
        temp = words[left:N] + words[:right - N]
    else:
        temp = words[left:right]
    res = min(res, temp.count('b'))
    left += 1
print(res)