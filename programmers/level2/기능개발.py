import math
from collections import deque

def solution(progresses, speeds):
    answer = []

    deploy = deque([math.ceil((100-a) / b) for a, b in zip(progresses, speeds)])
    # progresses + speeds * x >= 100
    # (100 - progresses) / speeds
    while deploy:
        current = deploy.popleft()
        count = 1
        while len(deploy) > 0:
            if current >= deploy[0]:
                deploy.popleft()
                count += 1
            else:
                break
        answer.append(count)

    return answer



if __name__ == '__main__':
    solution([93,30,55], [1,30,5])