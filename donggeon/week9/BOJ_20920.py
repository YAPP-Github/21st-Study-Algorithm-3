import sys
from collections import defaultdict
inp = lambda : sys.stdin.readline().rstrip()
# 길이가 M 이상인 것만 외운다
N, M = map(int, inp().split())
words = defaultdict(int)
for _ in range(N):
    word = inp()
    if len(word) >= M:
        words[word] += 1
for w in sorted(words.keys(), key=lambda x: (-words[x], -len(x), x)):
    print(w)