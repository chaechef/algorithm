def solution(n):
    nums = set(range(3, n+1, 2))
    for num in range(3, n+1, 2):
        if num in nums:
            nums -= set(range(num*2, n+1, num))

    return len(nums) + 1


if __name__ == "__main__":
    solution(10)