from collections import deque

def solution(priorities, location):
    answer = 0
    dq = deque([(i, priorities[i]) for i in range(len(priorities))])
    priorities.sort()
    count = 1

    while dq:
        curr = dq.popleft()

        if curr[1] == priorities[-1]:
            if curr[0] == location:
                return count
            else:
                priorities.pop()
                count += 1
        else:
            dq.append(curr)



print(solution([2, 1, 3, 2], 2))