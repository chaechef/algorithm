# def convert(n, base):
#     T = '012'
#     q, r = divmod(n, base)
#     print(q, r)
#     if q == 0:
#         return T[r]
#     else:
#         return convert(q, base) + T[r]

def solution(n):
    answer = ''
    covremain = {1: '1', 2: '2', 0: '4'}
    while n:
        n, r = divmod(n, 3)
        answer = covremain[r] + answer
        if r == 0:
            n -= 1

    return answer

if __name__ == '__main__':
    print(solution(5))