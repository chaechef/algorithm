def cus(num):
    s = str(num)
    if len(s) == 3:
        return int(s + s[0])
    else:
        return int(s * int((4 / len(s))))


def solution(numbers):

    numbers.sort(key=cus, reverse=True)

    ret = "".join(map(str,numbers))

    # if int(ret) == 0:
    #     return '0'
    return ret

print(solution([1000,1000]))

