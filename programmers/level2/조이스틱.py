
def caldist(char):
    return min(ord(char)- ord('A'), ord('Z')+1 - ord(char))

def solution(name):
    arr1 = [caldist(char) for char in name]
    arrsum = sum(arr1)
    tempsum = 0
    step = -1
    for a in arr1:
        if tempsum == arrsum:
            break
        tempsum += a
        step += 1
    ret = tempsum + step

    for i in range(1, len(name)):
        # i에서 되돌아가기
        tempsum = 0
        step = 0
        for j in range(0, i):
            tempsum += arr1[j]
        step += (i-1) * 2

        for j in range(len(name) - 1, i - 1, -1):
            if tempsum == arrsum:
                break
            tempsum += arr1[j]
            step += 1
        if tempsum + step < ret:
            ret = tempsum + step
    return ret

print(solution("JEROEN"))
# print(solution("JAN"))
print(solution("JAN"))
