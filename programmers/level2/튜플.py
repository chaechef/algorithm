import re
def solution(s):
    p = re.compile('\{(\d[,\d]*)\}')
    match = p.findall(s)
    arr = [list(map(int, s.split(','))) for s in match]
    arr.sort(key= lambda x: len(x))
    answer = []
    for tu in arr:
        for num in tu:
            if num not in answer:
                answer.append(num)

    return answer

solution("{{4,2,3},{3},{2,3,4,1},{2,3}}")