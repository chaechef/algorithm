from collections import deque
def solution(s):
    answer = 1000
    l = len(s) // 2 + 1
    for i in range(1, l):
        tstring = ""
        splitstring = deque([s[j:j+i] for j in range(0, len(s), i)])
        prev = splitstring.popleft()
        count = 1
        while splitstring:
            curr = splitstring.popleft()
            if prev == curr:
                count += 1
            else:
                if count > 1:
                    tstring += str(count)
                tstring += prev
                prev = curr
                count = 1
        if count > 1:
            tstring += str(count)
        tstring += prev

        if answer > len(tstring):
            answer = len(tstring)

    if len(s) == 1:
        return 1
    return answer

a = solution("a")
print(a)