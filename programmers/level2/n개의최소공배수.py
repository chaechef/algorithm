def gcd(a, b):
    if a < b:
        a, b = b, a
    while b:
        a, b = b, a % b
    return a

def solution(arr):
    if len(arr) == 1:
        return arr[0]

    a, b = arr.pop(), arr.pop()
    arr.append(a * b /gcd(a, b))
    ret = solution(arr)

    return int(ret)



print(solution([2,6,8,14]))