def solution(n, words):
    history = set([])
    prev = ""
    for idx, word in enumerate(words):
        if word in history:
            return [idx % n + 1, idx // n + 1]

        if prev != "" and prev[-1] != word[0]:
            return [idx % n + 1, idx // n + 1]

        history.add(word)
        prev = word

    return [0, 0]


print(solution(3, ['tank', 'kick', 'know', 'wheel', 'land', 'dream', 'mother', 'robot', 'tank']))