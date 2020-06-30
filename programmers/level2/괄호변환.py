def iscorret(p):
    stk = []
    for c in p:
        if not stk:
            stk.append(c)
            continue

        if c == '(':
            stk.append(c)
        else:
            if not stk:
                return -1
            else:
                stk.pop()

    if stk:
        return -1
    else:
        return 1

def reverse_remain(p):
    ans = ''
    for val in p:
        if val == '(':
            ans = ans + ')'
        else:
            ans = ans + '('
    return ans

def solution(p):
    if p == '':
        return ''

    left = right = 0
    for c in p:
        if left != 0 and right != 0 and left == right:
            break
        if c == '(':
            left += 1
        else:
            right += 1

    remain = p[:left + right]

    if iscorret(remain) == 1:
        return remain + solution(p[left + right:])
    else :
        return '(' + solution(p[left+right:]) + ')' + reverse_remain(remain[1:len(remain)-1])


print(solution('()))((()'))