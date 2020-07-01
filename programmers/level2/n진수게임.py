def base(num, b):
    ret = ""
    if num == 0:
        return '0'
    while num:
        temp = num % b
        if temp > 9:
            ret = str(chr(65 + temp - 10)) + ret
        else:
            ret = str(temp) + ret

        num //= b

    return ret


def solution(n, t, m, p):

    total = t * m
    curr = 0
    changedstring = ""
    while len(changedstring) < total:
        changedstring += base(curr,n)
        curr += 1
    changedstring = changedstring[:total]
    temp = [changedstring[i] for i in range(total) if i % m == p-1]
    answer = "".join(temp)

    return answer

print(solution(16, 16, 2, 1))
print(solution(2, 4, 2, 1))