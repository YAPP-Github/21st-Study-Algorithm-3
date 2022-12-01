import sys
inp = lambda : int(sys.stdin.readline())
# +, -, 공백(' ') 세가지 경우 가능
# 공백은 숫자 이어붙이기
# 자연수 오름차순 으로 1~N까지 숫자 이용
answer = []
# op 끼워 넣는 경우의 수 만들기
def dfs(depth, n, op:str):
    if depth == n:
        # 0이 나온 경우
        answer.append(''.join(op))
        return
    # 각 연산자 추가
    dfs(depth + 1, n, op + ' ' + str(depth+1))
    dfs(depth + 1, n, op + '+' + str(depth+1))
    dfs(depth + 1, n, op + '-' + str(depth+1))
K = inp()
for i in range(K):
    N = inp()
    dfs(1, N, '1')
    for k in range(len(answer)):
        temp = answer[k].replace(' ', '')
        if eval(temp) == 0:
            print(answer[k])
    if i != K-1: print()
    answer.clear()