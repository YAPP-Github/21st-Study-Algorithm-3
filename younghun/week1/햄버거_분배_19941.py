import sys

n, k = map(int, sys.stdin.readline().split())
table = list(sys.stdin.readline())[:-1]
people = []
answer = 0

for i in range(n):
    if table[i] == 'P':
        people.append(i)

for person in people:
    for i in range(max(0, person - k), min(person + k + 1, n)):  # 먹을 수 있는 범위의 햄버거만 탐색.
        if table[i] == 'H':
            table[i] = 'N'
            answer += 1
            break
print(answer)
