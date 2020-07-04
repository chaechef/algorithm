
def caldist(char):
    return min(ord(char)- ord('A'), ord('Z')+1 - ord(char))

def solution(name):
    arr1 = [caldist(char) for char in name]
    arr2 = [arr1[0]] + arr1[1:][::-1]

    namesum = sum(arr1)
    tempsum = 0
    ret = -1
    for val in arr1:
        if tempsum == namesum:
            break
        tempsum += val
        ret += val + 1

    tempsum = 0
    ret1 = -1
    for val in arr2:
        if tempsum == namesum:
            break
        tempsum += val
        ret1 += val + 1

    return min(ret, ret1)

print(solution("JEROEN"))
# print(solution("JAN"))
print(solution("AAA"))
