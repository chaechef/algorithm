def solution(phone_number):
    ret = '*' * len(phone_number[:-4]) + str(phone_number[-4:])
    return ret

if __name__ == "__main__":
    solution('01033334444')