
from collections import deque

n = int(input())
board = [[0] * n for _ in range(n)]
commands = ["" for _ in range(10001)]
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
t = 0
d = 0
time = 0
for i in range(int(input())):
    r, c = map(int, input().split(" "))
    board[r-1][c-1] = 1

for i in range(int(input())):
    idx, di = input().split(" ")
    commands[int(idx)] = di

snake = deque()
snake.append((0,0))
while True:
    py, px = snake[-1]
    ny, nx = py + dy[d], px + dx[d]
    if ny < 0 or ny >= n or nx < 0 or nx >= n:
        break

    if (ny,nx) in snake:
        break

    time += 1
    if commands[time] == "L":
        d -= 1
    if commands[time] == "D":
        d += 1
    if d == 4:
        d = 0
    if d == -1:
        d = 3

    if board[ny][nx] == 1:
        board[ny][nx] = 0
        snake.append((ny,nx))
        continue

    snake.append((ny,nx))
    snake.popleft()

for s in snake:
    y, x = s
    board[y][x] = "*"

print(time + 1)

