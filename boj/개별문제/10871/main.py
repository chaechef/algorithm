if __name__ == "__main__":
    in1 = list(map(int,input().split()))
    arr = list(map(int, input().split()))
    res = list(filter(lambda i: i < in1[1], arr))
    res = " ".join(list(map(str, res)))
    print(res)
