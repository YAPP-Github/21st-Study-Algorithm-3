import sys
input = sys.stdin.readline

S = input().rstrip() # BAAAAABAA
T = input().rstrip() # BAABAAAAAB

def check(word):
    if word == S: return 1
    if len(word) <= len(S): return 0

    result = 0
    if word[-1] == 'A':
        result = check(word[:-1])
    if result == 1:
        return 1
    if word[0] == 'B':
        temp = word[::-1]
        result = check(temp[:-1])
    return result
print(check(T))