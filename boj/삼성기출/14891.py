def rotate(t: str, clock: bool):
    if clock:
        return t[-1] + t[:-1]
    else:
        return t[1:] + t[0]


ts = [input() for _ in range(4)]
n = int(input())


def recursion(idx: int, c: list, clock: bool):

    if c[idx] == 1:
        return
    if idx - 1 >= 0 and ts[idx][6] != ts[idx-1][2] and c[idx-1] == 0:
        c[idx] = 1
        recursion(idx-1, c, not clock)
    if idx + 1 < 4 and ts[idx][2] != ts[idx+1][6] and c[idx+1] == 0:
        c[idx] = 1
        recursion(idx+1, c, not clock)
    ts[idx] = rotate(ts[idx], clock)


for _ in range(n):
    t, r = map(int, input().split())
    r = True if r == 1 else False
    check = [0] * 4
    recursion(t-1, check, r)

sum = 0
for i in range(4):
    if ts[i][0] == "1":
        sum += pow(2, i)

print(sum)