import sys
from collections import Counter, defaultdict
inp = lambda : sys.stdin.readline().rstrip()
# 알파벳 소문자와 숫자로 이루어진 문자열
# 1) 어떤 문자를 정확히 K개를 포함하는 가장 짧은 연속 문자열의 길이
# 2) 어떤 문자를 정확히 K개를 포함하고 문자열의 처음과 끝이 해당 문자로 같은 가장 긴 연속 문자열의 길이
for _ in range(int(inp())):
    W = inp()
    K = int(inp())
    word_dict = defaultdict(list)
    N = len(W)
    for i in range(N):
        word_dict[W[i]].append(i)
    answer = [sys.maxsize, -sys.maxsize]
    # 시간 초과 난 풀이
    # answer = sys.maxsize
    # count = Counter(W[0])
    # i, j = 0, 0
    # # 3번 문장 풀이
    # while i <= j < N:
    #     if max(count.values()) >= K:
    #         answer = min(answer, j - i + 1)
    #         if count[W[i]] == 1:
    #             del count[W[i]]
    #         else: count[W[i]] -= 1
    #         i += 1
    #     else:
    #         j += 1
    #         if j < N: count[W[j]] += 1
    # 4번 문장 풀이
    res = 0
    for word in word_dict.values():
        if len(word) < K: continue
        for i in range(len(word)-K+1):
            temp = word[i+K-1] - word[i] + 1
            if answer[0] > temp:
                answer[0] = temp
            if answer[1] < temp:
                answer[1] = temp
    if answer[0] < sys.maxsize and answer[1] > -sys.maxsize:
        print(*answer)
    else:
        print(-1)