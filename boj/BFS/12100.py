# Hello World
from collections import deque
import copy

n = int(input())
board = [list(map(int, input().split(" "))) for _ in range(n)]
queue = deque()
mm = 0
queue.append((copy.deepcopy(board), 0))


def hap(arr: [int], direct: bool):
    # 참이면 오른
    a = list(filter(lambda x: x != 0, arr))

    if direct:
        idx = len(a) - 1
        while idx > 0:
            if a[idx] == a[idx - 1]:
                a[idx] *= 2
                a[idx - 1] = 0
                idx -= 2
            else:
                idx -= 1
        a = list(filter(lambda x: x != 0, a))

        a = [0] * (len(arr) - len(a)) + a
    else:
        idx = 0
        while idx < len(a) - 1:
            if a[idx] == a[idx + 1]:
                a[idx] *= 2
                a[idx + 1] = 0
                idx += 2
            else:
                idx += 1
        a = list(filter(lambda x: x != 0, a))
        a = a + [0] * (len(arr) - len(a))

    return a

while queue:
    cboard, count = queue.popleft()
    if count == 5:
        mm = max(mm, max(map(max, cboard)))
        continue

    for direct in range(4):
        cdboard = copy.deepcopy(cboard)
        if direct == 0:
            for i in range(len(cboard)):
                cdboard[i] = hap(cboard[i], False)
        if direct == 1:
            for i in range(len(cboard)):
                cdboard[i] = hap(cboard[i], True)
        if direct == 2:
            for j in range(len(cdboard[0])):
                new = hap(list(zip(*cdboard))[j], True)
                for i in range(len(cdboard)):
                    cdboard[i][j] = new[i]
        if direct == 3:
            for j in range(len(cdboard[0])):
                new = hap(list(zip(*cdboard))[j], False)
                for i in range(len(cdboard)):
                    cdboard[i][j] = new[i]
        queue.append((cdboard, count + 1))

print(mm)