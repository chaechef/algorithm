def solution(s, n):
    asci = list(map(ord, s))
    ret = ""
    for val in asci:
        if ord('a') <= val <= ord('z'):
            ret += (chr((val - ord('a') + n) % 26 + ord('a')))
        elif ord('A') <= val <= ord('Z'):
            ret += (chr((val - ord('A') + n) % 26 + ord('A')))
        else:
            ret += " "
    return ret

if __name__ == '__main__':
    solution("a B z Z", 4)