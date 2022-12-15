import sys
from collections import deque

n, d, k, c = map(int, sys.stdin.readline().split())

sushi = [int(sys.stdin.readline()) for _ in range(n)]


def solution(n, d, k, c, sushi):
    answer = []
    choice = deque()

    for i in range(k):
        choice.append(sushi[i])
    kind = set(choice)
    kind.add(c)
    answer.append(len(kind))

    for i in range(1, n):
        choice.popleft()

        new_sushi = sushi[(i+k-1) % n]
        choice.append(new_sushi)

        kind = set(choice)
        kind.add(c)
        answer.append(len(kind))

    return max(answer)


print(solution(n, d, k, c, sushi))
