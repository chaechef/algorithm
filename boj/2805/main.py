import sys


def bisearch(target):
    left = 0
    right = maxheight
    temp = 0

    while left <= right:
        mid = int((left + right) / 2)
        sum = 0
        temp = mid
        for val in arr:
            if val > mid:
                sum += val-mid
        if sum == target:
            return mid
        elif sum > target:
            left = mid + 1
        else:
            right = mid - 1

    return right


if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())
    arr = [int(i) for i in sys.stdin.readline().split()]
    maxheight = max(arr)
    t1 = bisearch(m)
    print(t1)