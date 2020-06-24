def solution(s):
    countY = s.count('y') + s.count('Y')
    countX = s.count('p') + s.count('P')
    if countX == countY:
        return True
    return False

if __name__ == "__main__":
    solution('pPoooyY')