S = input()
T = input()
S_len = len(S)
T_len = len(T)
ret = 0

def dfs(word, word_len):
    global ret
    # 답이 나왔으면 바로 종료한다.
    if ret:
        return
    # 단어가 일치한다면 ret을 1로 변경한다.
    if word_len == S_len:
        if word == S:
            ret = 1
    # 단어의 길이가 같아질 때까지 글자를 제거한다.
    else:
        # 단어 제일 뒤가 A인 경우에는 A를 뺀다.
        if word[-1] == "A":
            dfs(word[:-1], word_len-1)
        # 단어 제일 앞이 B인 경우에는 B를 빼고 단어를 뒤집는다.
        if word[0] == "B":
            dfs(word[1:][::-1], word_len-1)

dfs(T, T_len)
print(ret)
