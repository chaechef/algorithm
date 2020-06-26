def convert(n, base):
    T = '012'
    q, r = divmod(n, base)
    print(q, r)
    if q == 0:
        return T[r]
    else:
        return convert(q, base) + T[r]

def solution(n):
    answer = ''
    cov = convert(n, 3)
    print(cov)
    return answer

if __name__ == '__main__':
    solution(3)