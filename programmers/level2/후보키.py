
def dcount(s1, s2):
    count = 0
    for a, b in zip(s1, s2):
        if a != b:
            count += 1

    return count

def solution(relation):
    answer = []
    colnum = len(relation[0])
    rownum = len(relation)
    combi = [bin(i)[2:].rjust(colnum,'0') for i in range(1,2**colnum)]
    print(combi)
    for c in combi:
        temp = [[val for idx, val in enumerate(row) if c[idx] == '1'] for row in relation]
        temp = ["".join(val) for val in temp]
        if len(set(temp)) == rownum:
            answer.append(c)

    answer = sorted(answer, key=lambda x: x.count('1'))
    checklist = [True] * len(answer)

    for i in range(len(answer)):
        for j in range(i+1, len(answer)):
            if dcount(answer[i], answer[j]) == 1:
                checklist[j] = False

    return checklist.count(True)

print(solution([['1'],['2']]))
# solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]])