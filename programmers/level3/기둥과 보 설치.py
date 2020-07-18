def is_gi_create(y, x, board):
    if y == 0 or board[y-1][x][0] == 1 or board[y][x-1][1] == 1 or board[y][x][1] == 1:
        return True
    return False

def is_bo_create(y, x, board):
    if board[y-1][x][0] == 1 or board[y-1][x+1][0] == 1 or (board[y][x-1][1] == 1 and board[y][x+1][1] == 1):
        return True
    return False

def is_gi_delete(y, x, board):
    board[y][x][0] = 0
    if is_gi_create(y+1,x, board) and is_bo_create(y+1,x, board) and is_bo_create(y+1,x-1,board):
        board[y][x][0] = 1
        return True
    board[y][x][0] = 1
    return False

def is_bo_delete(y, x, board):
    board[y][x][1] = 0
    if is_bo_create(y, x-1, board) and is_bo_create(y, x+1, board) and is_gi_create(y,x, board) and is_gi_create(y,x+1,board):
        board[y][x][1] = 1
        return True
    board[y][x][1] = 1
    return False


def solution(n, build_frame):
    answer = []
    board = [[[0, 0] for _ in range(n + 1)] for _ in range(n + 1)]
    for inst in build_frame:
        x, y, a, b = inst
        if b == 1:
            # 설치
            if a == 0 and is_gi_create(y,x,board):
                board[y][x][0] = 1
                # 기둥

            if a == 1 and is_bo_create(y,x, board):
                board[y][x][1] = 1
                # 보

        if b == 0:
            if a == 0 and is_gi_delete(y,x,board):
                board[y][x][0] = 0
            if a == 1 and is_bo_delete(y,x, board):
                board[y][x][1] = 0
            # 제거


    for i in range(n+1):
        for j in range(n+1):
            if board[i][j][0] != 0:
                # 앞에가 기둥
                answer.append([j, i, 0])
            if board[i][j][1] != 0:
                # 뒤에가 보
                answer.append([j, i, 1])

    answer.sort(key=lambda a: (a[0], a[1], a[2]))

    return answer


print(solution(5, [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]))
print(solution(5, [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]))