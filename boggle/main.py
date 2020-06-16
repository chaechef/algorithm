import sys


def inrange(y, x):
    if 0 <= y < 5 and 0 <= x < 5:
        return True
    return False


def recursion(word, y, x):
    dy = [-1, -1, -1, 0, 0, 1, 1, 1]
    dx = [-1, 0, 1, -1, 1, -1, 0, 1]

    for d in range(len(dy)):
        cy = y + dy[d]
        cx = x + dx[d]
        if inrange(cy, cx) and word[0] == board[cy][cx]:
            if len(word) == 1:
                return True
            if recursion(word[1:], cy, cx):
                return True
    else:
        return False


def hasword(word: str):
    for i in range(len(board)):
        for j in range(len(board)):
            if word[0] == board[i][j]:
                if recursion(word[1:], i, j):
                    return True
    else:
        return False


if __name__ == "__main__":
        tc = int(sys.stdin.readline())
        arr = []
        for _ in range(tc):
            board = [sys.stdin.readline().rstrip() for _ in range(5)]
            n = int(sys.stdin.readline())
            for _ in range(n):
                word = sys.stdin.readline().rstrip()
                if hasword(word):
                    print(word, "YES")
                else:
                    print(word, "NO")

