import sys
from collections import defaultdict

n, d, k, c = map(int, sys.stdin.readline().split())

sushi = [int(sys.stdin.readline()) for _ in range(n)]


def solution(n, d, k, c, sushi):
    choice = defaultdict(int)  # 초밥 선택정보를 딕셔너리로 관리
    choice[c] += 1  # 쿠폰으로 받는 초밥이 이미 먹었다고 가정

    for i in range(k):  # 초기 k개 초기화
        choice[sushi[i]] += 1
    answer = len(choice)

    for i in range(n):
        start = i
        next_sushi = (i+k) % n

        choice[sushi[start]] -= 1  # 시점에 있는 초밥 선택을 되돌림

        if choice[sushi[start]] == 0:  # 해당 초밥을 1개도 먹지 않았다면
            del choice[sushi[start]]  # 종류에 카운팅 되지 않도록 배제

        choice[sushi[next_sushi]] += 1  # 새로운 초밥 선택에 추가

        answer = max(answer, len(choice))  # 초밥 종류 수의 최대값 갱신
    return answer


print(solution(n, d, k, c, sushi))
