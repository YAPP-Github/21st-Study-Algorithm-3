import sys
N, r, c = map(int, sys.stdin.readline().split())
cnt = 0
def traverse(x, y, z):
    global cnt
    if z == 1:
        if x == r and y == c:
            print(cnt)
            exit()
        cnt += 1

        return
    else:
        if x <= r < x + z // 2:
            if y <= c < y + z // 2:
                traverse(x, y, z // 2)
            else:
                # (z // 2) ** 2
                cnt += (z ** 2) // 4
                traverse(x, y + z // 2, z // 2)
        else:
            if y <= c < y + z // 2:
                cnt += (z ** 2) // 2
                traverse(x + z // 2, y, z // 2)
            else:
                cnt += 3 * (z ** 2) // 4
                traverse(x + z // 2, y + z // 2, z // 2)
traverse(0, 0, 2 ** N)