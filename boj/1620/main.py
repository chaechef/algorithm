import sys

if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())
    dic = {}
    dic2 = {}
    for i in range(1,n+1):
        dic[i] = sys.stdin.readline().strip()
        dic2[dic[i]] = i

    for _ in range(m):
        query = sys.stdin.readline().strip()
        if query.isdigit():
            print(dic[int(query)])
        else:
            print(dic2[query])

