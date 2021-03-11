import sys


def bisearch(target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = int((left + right) / 2)
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return -1


if __name__ == "__main__":
    n = int(sys.stdin.readline())
    arr = [int(i) for i in sys.stdin.readline().split()]
    m = int(sys.stdin.readline())
    test = [int(i) for i in sys.stdin.readline().split()]
    arr = sorted(arr)
    for val in test:
            if bisearch(val) != -1:
                print(1)
            else:
                print(0)
