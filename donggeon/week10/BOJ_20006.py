import sys
inp = lambda : sys.stdin.readline().split()
# 입장 신청하였을 때 매칭이 가능한 방이 없다면 새로운 방 생성시키고 입장
## 처음 입장한 플레이어 기준/ 레벨 기준 +- 10까지 입장가능
# 방의 정원 모두 찰 때 까지 대기
## 방이 여러 개 가능하면 먼저 생성된 방으로
# 정원 모두 차면 시작
games = []
p, m = map(int, inp())
for _ in range(p):
    l_str, n = map(str, inp())
    l = int(l_str)
    check = False
    for g in games:
        if len(g) == m:
            continue
        if l - 10 <= g[0][0] <= l + 10:
            g.append((l, n))
            check = True
            break
    if not check:
        games.append([(l, n)])
for i in range(len(games)):
    if len(games[i]) == m:
        print("Started!")
    else:
        print("Waiting!")
    for g in sorted(games[i], key=lambda x: x[1]):
        print(g[0], g[1])