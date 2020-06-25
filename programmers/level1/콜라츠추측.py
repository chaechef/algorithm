def solution(num):
    answer = 0
    for i in range(500):
        if num == 1:
            return i
        if num % 2 == 0:
            num /= 2
        else:
            num = num * 3 + 1

    return -1

if __name__ == "__main__":
    print(solution(626331))
