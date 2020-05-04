import sys

if __name__=="__main__":
    n = int(input())
    lists = list(map(int, input().split()))
    maxvalue = max(lists)
    lists = list(map(lambda i: i / maxvalue * 100, lists))
    print(sum(lists) / len(lists))

