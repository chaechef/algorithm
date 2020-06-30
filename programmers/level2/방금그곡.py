import re

def gettime(s,e):
    sh, sm = map(int, s.split(":"))
    eh, em = map(int, e.split(":"))
    return (eh-sh) * 60 + em - sm

def solution(memo, musicinfos):
    answer = ''
    mintime = 0
    memo1 = re.findall('[A-G]#?', memo)
    for line in musicinfos:
        st, et, title, melody = line.split(",")
        time = gettime(st, et)
        melody = re.findall('[A-G]#?', melody)
        if time < len(melody):
            melody = melody[:time]
        else:
            q, r = divmod(time, len(melody))
            melody = melody * q + melody[:r]
        if len(memo1) > len(melody):
            continue
        for i in range(len(melody) - len(memo1) + 1):
            for j in range(len(memo1)):
                if memo1[j] != melody[i+j]:
                    break
            else:
                if mintime < time:
                    answer = title
                    mintime = time
                break

    if answer == "":
        return '(None)'

    return answer

print(solution(	"ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
print(solution(	"ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
print(solution(	"CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))