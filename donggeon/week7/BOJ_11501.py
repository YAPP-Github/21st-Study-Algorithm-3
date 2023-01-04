import sys
inp = lambda: sys.stdin.readline()
for _ in range(int(inp())):
    N = int(inp())
    money = list(map(int, inp().split()))
    # 갖고 있다가 최대로 이익 볼 수 있을 때 판다
    res, money_max = 0, 0
    for i in range(N - 1, -1, -1):
        if money_max < money[i]:
            money_max = money[i]
        else:
            res += money_max - money[i]
    print(res)
