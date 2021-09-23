
def check_available_road(arr: list, l: int) -> bool:
    idx = 0
    slide_check = [0] * len(arr)
    while idx < len(arr):
        if idx == len(arr) - 1:
            return True
        if arr[idx] == arr[idx+1]:
            idx += 1
            continue
        if arr[idx] == arr[idx+1] + 1:
            nextvalue = arr[idx+1]
            for i in range(idx+1, idx+1+l):
                if i >= len(arr):
                    return False
                if arr[i] != nextvalue:
                    return False
                slide_check[i] = 1
            idx = idx + l
        elif arr[idx] == arr[idx+1] - 1:
            for i in range(idx + 1 - l, idx + 1):
                if i < 0:
                    return False
                if arr[i] != arr[idx]:
                    return False
                if slide_check[i] == 1:
                    return False
                slide_check[i] = 1
            idx += 1
        else :
            return False
    return True


n , l = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
sum = 0
for b in board:
    rb = list(reversed(b))
    if check_available_road(rb, l) or check_available_road(b, l):
        sum += 1

for b in list(zip(*board)):
    rb = list(reversed(b))
    if check_available_road(rb, l) or check_available_road(b, l):
        sum += 1
print(sum)