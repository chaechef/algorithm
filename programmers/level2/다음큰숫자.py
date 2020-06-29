def basetwo(num):
    ret = ""
    while num:
        ret = str(num % 2) + ret
        num = num // 2
    return ret


def solution(n):
    answer = 0
    curr = n + 1
    countone = basetwo(n).count('1')
    while True:
        if basetwo(curr).count('1') == countone:
            return curr
        curr += 1

print(solution(15))