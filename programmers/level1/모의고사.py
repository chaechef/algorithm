def solution(answers):
    s = [[],[],[]]
    s[0] = [1,2,3,4,5]
    s[1] = [2,1,2,3,2,4,2,5]
    s[2] = [3,3,1,1,2,2,4,4,5,5]

    correct = [0] * 3

    for i in range(3):
        idx = 0
        for j in range(len(answers)):
            idx = j % len(s[i])
            if s[i][idx] == answers[j]:
                correct[i] += 1

    ret = [idx+1 for idx, val in enumerate(correct) if val == max(correct)]

    return ret



if __name__ == "__main__":
    print(solution([1,3,2,4,2]))