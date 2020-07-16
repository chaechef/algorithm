from collections import deque

def solution(operations):
    answer = []
    arr = []

    for oper in operations:
        inst, num = oper.split(' ')
        if inst == 'I':
            arr.append(int(num))
        if inst == 'D' and len(arr) > 0:
            if num == '-1':
                arr.sort()
                arr.pop(0)
            elif num == '1':
                arr.sort()
                arr.pop()

    arr.sort()
    if not arr:
        return [0, 0]

    answer = [arr[-1], arr[0]]
    return answer

print(solution(['I 16','D 1']))
print(solution(['I 7','I 5','I -5','D -1']))