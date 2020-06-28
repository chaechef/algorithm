from collections import deque
from itertools import permutations
def solution(numbers):
    answer = ''
    a, b, c = [], [], []
    for val in numbers:
        if val < 10:
            a.append(val)
        elif val < 100:
            b.append(val)
        else:
            c.append(val)
    a = list(map(int, sorted(list(map(str, a)), reverse=True)))
    b = list(map(int, sorted(list(map(str, b)), reverse=True)))
    c = list(map(int, sorted(list(map(str, c)), reverse=True)))

    a = deque(a)
    b = deque(b)
    c = deque(c)
    while a or b or c:

        temp = []
        tempidx = []
        if a:
            temp.append(a[0])
            tempidx.append(0)
        if b:
            temp.append(b[0])
            tempidx.append(1)
        if c:
            temp.append(c[0])
            tempidx.append(2)

        per = [int("".join(map(str, val))) for val in list(permutations(temp, len(temp)))]

        midx = per.index(max(per))
        target = 0
        if len(tempidx) == 3:
            target = tempidx[midx // 2]
        elif len(tempidx) == 2:
            target = tempidx[midx // 1]
        else:
            target = tempidx[0]

        if target == 0:
            answer += str(a.popleft())
        elif target == 1:
            answer += str(b.popleft())
        else:
            answer += str(c.popleft())
    if int(answer) == 0:
        return '0'
    return answer




print(solution([999,9,998]))