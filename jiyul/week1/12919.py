import sys
input=sys.stdin.readline
S=list(input())
T=list(input())

def convert(t):
    global flag
    if len(t)==len(S): 
        if t==S:
            print(1)
            exit(0)
        return

    if t[0]=='B':
        t=t[::-1]
        t.pop()
        convert(t)
        t.append('B')
        t=t[::-1]

    if t[-1]=='A':
        t.pop()
        convert(t)
        t.append('A')

convert(T)
print(0)