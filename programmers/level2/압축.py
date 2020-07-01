def solution(msg):
    lzw = {chr(65+i): i+1 for i in range(26)}
    maxidx = 27
    answer = []
    start, end = 0, 1

    while start < end:
        if msg[start:end] in lzw:
            if end == len(msg):
                answer.append(lzw[msg[start:end]])
                break
            end += 1
        else:
            answer.append(lzw[msg[start:end-1]])
            lzw[msg[start:end]] = maxidx
            maxidx += 1
            start = end - 1

    return answer

solution('TOBEORNOTTOBEORTOBEORNOT')