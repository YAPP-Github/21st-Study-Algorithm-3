import sys
inp = lambda : sys.stdin.readline().rstrip()
# 모음(a,e, i, o, u) 하나를 반드시 포함
# 모음이 3개 연속 혹은 자음이 3개 연속 오면 안됨
# 같은 글자가 연속으로 두번 오면 안되나 ee, oo는 허용
vowel = ['a', 'i', 'e', 'o', 'u']
while True:
    line = inp()
    if line == 'end': break
    check = True
    # 모음 한 개라도 있는지 판단
    # 3개 연속 있는거 판단 (자음 세 개, 모음 세 개)
    v_check = False
    v_count, c_count = 0, 0
    for i in range(len(line)):
        if i >= 1:
            if line[i] != 'e' and line[i] != 'o' and line[i] == line[i-1]:
                check = False
                break
        if line[i] in vowel:
            v_check = True
            v_count += 1
            c_count = 0
            if v_count == 3:
                check = False
                break
        else:
            v_count = 0
            c_count += 1
            if c_count == 3:
                check = False
                break

    temp = '<' + line + '> '
    temp += 'is acceptable.' if check and v_check else 'is not acceptable.'
    print(temp)
