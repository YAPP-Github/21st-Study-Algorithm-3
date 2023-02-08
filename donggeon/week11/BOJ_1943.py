# 돈 똑같이 나누기/ 불가능한 경우도 존재
import sys
inp = lambda : sys.stdin.readline()
for _ in range(3):
    N = int(inp())
    coins = [tuple(map(int, inp().split())) for _ in range(N)]
    # 전체 가치 구하기
    ## 10 5
    ## 50 1
    ## 100 2
    total = sum(t * c for t, c in coins)
    if total % 2:
        print(0)
        continue
    target = total // 2
    dp = [1] + [0 for _ in range(target)]
    check = False
    for coin, cnt in coins:
        if check: break
        for i in range(target, coin - 1, -1):
            if check: break
            # 현재 동전을 사용하면 가능한 경우 존재
            if dp[i - coin]:
                for j in range(cnt):
                    if target > i + coin * j:
                        dp[i + coin * j] = 1
                    elif target == i + coin * j:
                        dp[target] = 1
                        check = True
                        break
    print(dp[target])