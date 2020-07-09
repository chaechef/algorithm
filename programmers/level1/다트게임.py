import re
def solution(dartResult):
    tok = re.findall('(\d+)([DST])([*#]?)', dartResult)
    bonus = {'S':1, 'D':2, 'T':3}
    option = {'#' : -1, '*': 2, '': 1}
    print(tok)
    scores = [0] * 3
    for i in range(3):
        scores[i] = int(tok[i][0]) ** bonus[tok[i][1]] * option[tok[i][2]]
        if tok[i][2] == '*' and i > 0:
            scores[i-1] *= 2

    return sum(scores)



if __name__ == '__main__':
    solution('1D2S#10S')