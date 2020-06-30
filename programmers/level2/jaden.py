def solution(s):
    ret = []
    for s in s.split(" "):
        if s != "" and not s[0].isdigit():
            ret.append(s.title())
        else:
            ret.append(s)

    return " ".join(ret)

solution("   3for the  last week")