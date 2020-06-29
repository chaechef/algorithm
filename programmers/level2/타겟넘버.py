def recursion(numbers, target, sum, idx):
    if idx == len(numbers):
        if sum == target:
            return 1
        else:
            return 0

    return recursion(numbers, target, sum + numbers[idx], idx+1) + recursion(numbers, target, sum - numbers[idx], idx+1)


def solution(numbers, target):
    answer = recursion(numbers, target, 0, 0)
    return answer


solution([1, 1, 1, 1, 1], 3)