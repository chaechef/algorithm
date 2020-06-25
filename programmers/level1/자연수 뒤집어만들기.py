def solution(n):
    ret = [int(i) for i in str(n)]
    ret = [str(i) for i in sorted(ret, reverse=True)]

    return "".join(ret)

if __name__ == '__main__':
    solution(12345)