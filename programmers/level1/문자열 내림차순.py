def solution(s):
    answer = ''
    print(sorted(s))
    return sorted(s, reverse=True)

if __name__ == "__main__":
    solution("ZAbcdefg")