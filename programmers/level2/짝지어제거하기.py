

def solution(s):
    stk = [s[0]]

    for i in range(1, len(s)):
        if not stk:
            stk.append(s[i])
            continue

        if s[i] != stk[-1]:
            stk.append(s[i])
        else:
            stk.pop()

    if stk:
        return 0
    else:
        return 1

print(solution('bxbc'))