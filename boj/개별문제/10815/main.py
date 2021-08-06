import sys


def biSearch(target):
    left = 0
    right = n-1

    while left <= right:
        mid = int((left + right) / 2)
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            right = mid -1
        else:
            left = mid + 1
    return -1



if __name__ == "__main__":
    n = int(sys.stdin.readline())
    arr = sorted([int(i) for i in sys.stdin.readline().split()])
    m = int(sys.stdin.readline())
    checklist = [int(i) for i in sys.stdin.readline().split()]
    results = [0 for i in range(m)]

    for idx, val in enumerate(checklist):
        if biSearch(val) == -1:
            results[idx] = 0
        else:
            results[idx] = 1

    print(" ".join(map(str, results)))
