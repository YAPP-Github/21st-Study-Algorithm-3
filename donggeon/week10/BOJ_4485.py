import sys, heapq
inp = lambda : sys.stdin.readline()
# 얻은 도둑 루피 최소화 해서 종료 지점으로 이동
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
cnt = 0
while True:
    n = int(inp())
    cnt += 1
    ## 0 입력 받으면 종료
    if not n: break
    maps = [list(map(int, inp().split())) for _ in range(n)]
    distances = [[sys.maxsize] * n for _ in range(n)]
    distances[0][0] = maps[0][0]
    q = []
    heapq.heappush(q, (distances[0][0], 0, 0))
    while q:
        cur_distance, x, y = heapq.heappop(q)
        if x == y == n-1:
            print(f"Problem {cnt}: {distances[n - 1][n - 1]}")
            break
        if distances[x][y] < cur_distance: continue
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n: continue
            temp_distance = cur_distance + maps[nx][ny]
            if temp_distance < distances[nx][ny]:
                distances[nx][ny] = temp_distance
                heapq.heappush(q, (temp_distance, nx, ny))
    # maps와 dp 초기화
    # maps = [list(map(int, inp().split())) for _ in range(n)]
    # dp = [[maps[0][0]] * n for _ in range(n)]
    # for i in range(n):
    #     for j in range(n):
    #         if i == j == 0: continue
    #         # 첫 행
    #         if not i:
    #             dp[i][j] = dp[i][j-1] + maps[i][j]
    #         elif not j:
    #             dp[i][j] = dp[i-1][j] + maps[i][j]
    #         else:
    #             dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + maps[i][j]
    # print("Problem" , cnt , ":" , dp[n-1][n-1])


