def solution(s):
    stk = 0
    if len(s) == 1:
        return False
    if s.count('(') != s.count(')'):
        return False

    for c in s:
        if c == '(':
            stk += 1
        else:
            if stk == 0:
                return False
            else:
                stk -= 1

    return True


print(solution('('))