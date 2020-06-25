def change(string):
    newstring = [s.upper() if i % 2 == 0 else s.lower() for i, s in enumerate(string)]
    return "".join(newstring)

def solution(s):
    words = s.split(" ")
    transform = [change(word) for word in words]
    answer = ''
    return ' '.join(transform)

if __name__ == '__main__':
    solution("   aaaaaaaaa  sdf  bbbb  ccc dd e")