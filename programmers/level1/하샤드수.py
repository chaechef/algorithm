def solution(x):
    s = sum([int(i) for i in str(x)])
    if x % s == 0:
        return True
    return False

if __name__ == '__main__':
    solution(10)