def solution(s):
    arr = list(map(int, s.split(" ")))
    arr.sort()
    answer = f'{arr[0]} {arr[-1]}'
    return answer

print(solution("1 2 -3 4"))