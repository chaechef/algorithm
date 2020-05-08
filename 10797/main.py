import sys

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    arr = [int(i) for i in sys.stdin.readline().split()]
    res = 0
    for val in arr:
        if val == n:
            res += 1
    print(res)