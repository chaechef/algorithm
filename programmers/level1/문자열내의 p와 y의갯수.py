def solution(s):
    return True if s.lower().count('y') == s.lower().count('p') else False


if __name__ == "__main__":
    print(solution('pPoooyY'))