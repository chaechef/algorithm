import re
def solution(dartResult):
    p = re.compile('\d+[SDT][*#]*')
    m = p.findall(dartResult)
    ret = [0] * 3

    for idx, val in enumerate(m):
        p1 = re.compile('\d+')
        p2 = re.compile('[S|D|T]')
        p3 = re.compile('[*|#]')
        m1 = p1.findall(val)[0]
        m2 = p2.findall(val)[0]
        m3 = ""
        if len(p3.findall(val)) > 0:
            m3 = p3.findall(val)[0]
        score = 0
        if m2 == 'S':
            score = int(m1) ** 1
        elif m2 == 'D':
            score = int(m1) ** 2
        else:
            score = int(m1) ** 3

        ret[idx] = score

        if m3 == '*':
            if idx - 1 >= 0:
                ret[idx-1] *= 2
            ret[idx] *= 2
        elif m3 == '#':
            ret[idx] *= -1


    return sum(ret)

if __name__ == '__main__':
    solution('1D2S#10S')