def solution(nums):
    numset = set(nums)

    if len(numset) > int(len(nums) // 2):
        return int(len(nums) // 2)
    else:
        return len(numset)

print(solution([1,1,1,2,2,2]))