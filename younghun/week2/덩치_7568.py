import sys

n = int(sys.stdin.readline())
people = []
rank = {}

for _ in range(n):
    people.append(list(map(int, sys.stdin.readline().split())))

for i in range(n):
    rank[i] = 1

for i in range(n):
    a_weight, a_height = people[i]

    for j in range(n):
        b_weight, b_height = people[j]

        if b_weight > a_weight and b_height > a_height:
            rank[i] += 1

for value in rank.values():
    print(value, end=' ')
