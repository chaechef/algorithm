from itertools import combinations

def make_prime_number(n):
    arr = set([i for i in range(3, n+1, 2)])
    for i in [i for i in range(3, n+1, 2)]:
        if i in arr:
            arr -= set([j for j in range(i*2, n+1, i)])
    return arr


def solution(nums):
    primeset = make_prime_number(3000)
    combiset = combinations(nums, 3)
    answer = 0
    for one in combiset:
        if sum(one) in primeset:
            answer += 1

    return answer


print(solution([1,2,7,6,4]))