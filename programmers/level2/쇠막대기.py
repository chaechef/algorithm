def solution(arrangement):
    answer = 0
    stk = []
    for i, c in enumerate(arrangement):
        if c == '(':
            stk.append('(')
        else:
            if i > 0 and arrangement[i-1] == '(':
                stk.pop()
                answer += len(stk)
            else:
                answer += 1
                stk.pop()


    return answer

if __name__ == '__main__':
    solution('()(((()())(())()))(())')
