import sys

if __name__ == "__main__":
    a, b, v = map(int, sys.stdin.readline().split())
    k = (v - b) / (a - b)
    print(int(k) if k == int(k) else int(k)+1)