import re
def tint(num):
    if num == '':
        return 0
    else:
        return int(num)

def solution(files):
    answer = []
    for file in files:
        print(file)
        parsed = re.findall('([\D\s.-]+)(\d*)([.a-zA-Z\d\s-]*)', file)[0]
        print(parsed)
        answer.append(parsed)

    answer.sort(key=lambda a: (a[0].lower(), tint(a[1])))
    answer = ["".join(one) for one in answer]

    return answer

# print(solution( ['img12.png', 'img10.png', 'img02.png', 'img1.png', 'IMG01.GIF', 'img2.JPG'])),
print(solution(['F-5 Freedom Fighter', 'B-50 Superfortress', 'A-10 Thunderbolt II', 'F-14 Tomcat']))