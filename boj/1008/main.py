import sys

if __name__ == "__main__":
    a = list(map(int, sys.stdin.readline().strip().split()))
    print(a[0] / a[1])
