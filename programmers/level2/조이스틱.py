
def caldist(char):
    return min(ord(char)- ord('A'), ord('Z')+1 - ord(char))

def solution(name):
    counts = [caldist(char) for char in name]
    arr1 = [counts[0]] + counts[1:][::-1]

    while arr1:
        if arr1[-1] == 0:
            arr1.pop()
        else:
            break
    while counts:
        if counts[-1] == 0:
            counts.pop()
        else:
            break

    ret = min(sum(arr1) + len(arr1)-1, sum(counts) + len(counts) - 1)
    if ret == -1:
        ret= 0
    return ret


# print(solution("JEROEN"))
# print(solution("JAN"))
print(solution("A"))
