def solution(a, b):
    if a > b:
        a, b = b, a
    return sum(range(a, b+1))

if __name__ == '__main__':
    solution(3,5)