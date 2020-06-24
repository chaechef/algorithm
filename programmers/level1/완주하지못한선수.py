def solution(participant, completion):
    pdick = {val: 0 for val in participant}
    for val in participant:
        pdick[val] += 1

    for val in completion:
        if pdick[val] == 0:
            return val
        pdick[val] -= 1

    for key in pdick.keys():
        if pdick[key] != 0:
            return key


if __name__ == "__main__":
    print(solution(['leo', 'kiki', 'eden', 'leo'], ['eden', 'kiki']))

