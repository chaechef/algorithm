import sys

if __name__ == "__main__":
    arr = [[i for i in sys.stdin.readline().strip()]for _ in range(5)]
    ans = ""
    for i in range(0,16):
        for j in range(5):
            if len(arr[j]) > i:
                ans += arr[j][i]
    print(ans)