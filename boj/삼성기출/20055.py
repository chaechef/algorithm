n, k = map(int, input().split())
arr = list(map(int, input().split()))
robot = [0] * 2 * n
loop = 1

while True:


    arr = [arr[-1]] + arr[:-1]
    robot = [robot[-1]] + robot[:-1]

    if robot[n-1] == 1:
        robot[n-1] = 0

    for i in reversed(range(n-1)):
        if robot[i] == 1 and robot[i+1] == 0 and arr[i+1] > 0:
            robot[i+1] = 1
            robot[i] = 0
            arr[i+1] -= 1

    if arr[0] > 0:
        arr[0] -= 1
        robot[0] = 1

    if robot[n-1] == 1:
        robot[n-1] = 0

    if arr.count(0) >= k:
        break
    loop += 1


print(loop)