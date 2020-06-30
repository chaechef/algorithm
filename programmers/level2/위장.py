from itertools import combinations

def solution(clothes):
    answer = 1
    clotheset = {}
    for cloth in clothes:
        if cloth[1] in clotheset:
            clotheset[cloth[1]] += 1
        else:
            clotheset[cloth[1]] = 1

    valuelist = [val + 1 for val in list(clotheset.values())]

    for val in valuelist:
        answer *= val
    return answer-1

solution([['yellow_hat', 'headgear'], ['blue_sunglasses', 'eyewear'], ['green_turban', 'headgear']])