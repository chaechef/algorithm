def solution(skill, skill_trees):
    answer = 0
    prior = {}
    for i, c in enumerate(skill):
        prior[c] = i + 1

    for skill in skill_trees:
        curr = 0
        for char in skill:
            if char not in prior:
                continue
            if prior[char] -1 == curr:
                curr = prior[char]
            else:
                break
        else:
            answer += 1

    return answer


solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"])