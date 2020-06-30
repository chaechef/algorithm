
def solution(record):
    answer = []
    message = {0: '님이 들어왔습니다.', 1: '님이 나갔습니다.'}
    nickname = {}

    for line in record:
        arr = line.split(" ")
        if arr[0] == 'Enter':
            nickname[arr[1]] = arr[2]
            answer.append((0, arr[1]))

        elif arr[0] == 'Leave':
            answer.append((1, arr[1]))
        else:
            nickname[arr[1]] = arr[2]



    answer = [nickname[val[1]] + message[val[0]] for val in answer]
    return answer


print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))