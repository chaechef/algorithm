def solution(number, k):
    flag = 0
    for i in range(0, k):
        for j in range(flag, len(number)-1):
            if number[j] < number[j+1]:
                flag = j - 1 if j - 1 >= 0 else 0
                number = number[:j] + number[j+1:]
                break
        else:
            number = number[:len(number) - (k-i)]
            break

    return number

print(solution("1231234", 3))
