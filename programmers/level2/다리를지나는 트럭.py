from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque([0] * bridge_length)
    truck_weights = deque(truck_weights)
    bsum = 0
    while truck_weights or bsum != 0:
        wait = 0
        if truck_weights:
            wait = truck_weights[0]
        answer += 1
        bsum -= bridge[0]
        bridge.popleft()
        if bsum + wait <= weight:
            if truck_weights:
                bsum += truck_weights[0]
                bridge.append(truck_weights.popleft())
        else:

            bridge.append(0)
    return answer

a = solution(100, 100, [10,10,10,10,10,10,10,10,10,10])
print(a)