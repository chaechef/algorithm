
def solution(n, m):
    cn, cm = n, m
    if m > n:
        n, m = m, n
    while m > 0:
        n, m = m, n % m
    return [n, cn * cm / n]


if __name__ == "__main__":
    solution(3,12)
