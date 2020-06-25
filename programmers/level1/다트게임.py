import re
def solution(dartResult):
    p = re.compile('(\d+)([SDT])([*#]*)')
    m = p.findall(dartResult)
    ret = [0] * 3
    bonus = {'S' : 1, 'D': 2, 'T': 3}
    option = {'*' : 2, '#' : -1, "": 1}
    for idx, val in enumerate(m):
        print(idx,val)
        if idx > 0 and val[2] == '*':
            ret[idx-1] *= 2
        ret[idx] = int(val[0]) ** bonus[val[1]] * option[val[2]]

    return sum(ret)

if __name__ == '__main__':
    solution('1D2S#10S')