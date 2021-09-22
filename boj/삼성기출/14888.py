from itertools import permutations

def calc(arr: list, oper: list):
    ret = arr[0]
    for i in range(1, len(arr)):
        if oper[i-1] == "+":
            ret += arr[i]
        if oper[i-1] == "-":
            ret -= arr[i]
        if oper[i-1] == "*":
            ret *= arr[i]
        if oper[i-1] == "/":
            ret = int(ret / arr[i])
    return ret





n = int(input())
arr = list(map(int, input().split()))
opers = list(map(int, input().split()))
opers = opers[0] * ["+"] + opers[1] * ["-"] + opers[2] * ["*"] + opers[3] * ["/"]
mmax = -2000000000
mmin = 2000000000
for oper in list(permutations(opers)):
    temp = calc(arr, oper)
    mmax = max(mmax, temp)
    mmin = min(mmin, temp)

print(mmax)
print(mmin)