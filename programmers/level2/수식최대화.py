import re
from itertools import permutations

def cal(left, right, op):
    if op == '+':
        return left + right
    elif op == '-':
        return left - right
    else:
        return left * right

def solution(expression):
    answer = 0
    numbers = list(map(int, re.findall('\d+', expression)))
    operators = re.findall('\D', expression)
    odict = {}
    priorities = list(permutations([0, 1, 2]))

    for priority in priorities:
        odict['+'], odict['-'], odict['*'] = priority
        nstack = [numbers[0]]
        ostack = []

        for i in range(len(operators)):
            if not ostack:
                ostack.append(operators[i])
                nstack.append(numbers[i+1])
                continue
            while ostack and odict[ostack[-1]] >= odict[operators[i]]:
                r = nstack.pop()
                l = nstack.pop()
                ret = cal(l, r, ostack.pop())
                nstack.append(ret)

            ostack.append(operators[i])
            nstack.append(numbers[i+1])

        while ostack:
            r = nstack.pop()
            l = nstack.pop()
            ret = cal(l, r, ostack.pop())
            nstack.append(ret)

        if abs(nstack[0]) > answer:
            answer = abs(nstack[0])

    return answer


print(solution("100-200*300-500+20"))