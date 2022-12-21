import sys
inp = lambda : sys.stdin.readline().rstrip()
N, M = map(int, inp().split())
# 새로운 키워드 작성
## 키워드 중 메모장에 있었던 키워드 삭제
## 없었으면 걍 넘기기

## 키워드 딕셔너리에 값들 넣기
keyword_set = {inp() for _ in range(N)}
for _ in range(M):
    keyword_list = list(inp().split(','))
    for k in keyword_list:
        if k not in keyword_set: continue
        keyword_set.remove(k)
    print(len(keyword_set))