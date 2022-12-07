import sys
from collections import defaultdict

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

cities = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
plan = list(map(int, sys.stdin.readline().split()))  # 여행 계획


def solution(n, m, cities):
    if m == 1 and n > 0:  # 도시 하나만 방문할 계획이고 해당 도시가 존재하면 YES
        return "YES"

    graph = defaultdict(list)

    for i in range(n):
        for j in range(n):
            if cities[i][j] == 1:
                graph[i + 1].append(j + 1)

    for i in range(m - 1):  # 각 여행 계획에 대하여 출발점과 목적지를 정의.
        start = plan[i]
        destination = plan[i + 1]

        stack = [start]
        visited = [False] * (n+1)
        visited[start] = True
        is_reachable = False

        while stack:  # DFS 탐색
            city = stack.pop()
            visited[city] = True

            if city == destination:  # 목적지에 도착하면 탐색 중지하고 다음 여행계획으로 넘어감.
                is_reachable = True
                break

            for item in graph[city]:
                if not visited[item]:
                    stack.append(item)

        if not is_reachable:  # 만약 DFS로 전체 탐색해도 목적지에 도달 할 수 없다면 NO
            return "NO"
    return "YES"


print(solution(n, m, cities))
