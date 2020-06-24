def solution(a, b):
    days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    sum = b + 4
    for i in range(0, a - 1):
        sum += days[i]

    ret = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']

    return ret[sum % 7]


if __name__ == "__main__":
    solution(1,1)
    solution(1,7)
    solution(5,24)