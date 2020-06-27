from itertools import permutations

def prime_set(num):
    nums = set([i for i in range(3, num+1, 2)])

    for i in [i for i in range(3, num+1, 2)]:
        if i in nums:
            nums -= set([j for j in range(i*2, num+1, i)])

    nums.add(2)
    return nums

def solution(numbers):
    answer = 0
    numset = set([])

    for i in range(1, len(numbers)+1):
        numset |= set([int("".join(val)) for val in list(permutations(numbers, i))])

    sprime = prime_set(max(numset))
    for num in numset:
        if num in sprime:
            answer += 1

    return answer


print(solution("17"))