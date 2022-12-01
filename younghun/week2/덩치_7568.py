import sys

n = int(sys.stdin.readline())
people = []
rank = {}

for _ in range(n):
    people.append(list(map(int, sys.stdin.readline().split())))

for i in range(n):
    people[i].append(i)
    rank[i] = 1

for person_a in people:
    a_weight, a_height, person_a_id = person_a

    for person_b in people:
        b_weight, b_height, person_b_id = person_b

        if b_weight > a_weight and b_height > a_height:
            rank[person_a_id] += 1

for value in rank.values():
    print(value, end=' ')
