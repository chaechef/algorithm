def nexthand(left, right, next, hand):
    lcount = abs(left[0]- next[0]) + abs(left[1] - next[1])
    rcount = abs(right[0]- next[0]) + abs(right[1] - next[1])

    if lcount > rcount:
        return 'right'
    elif rcount > lcount:
        return 'left'
    else:
        return hand

def solution(numbers, hand):
    answer = ''
    board = [(0, 1), (3, 0), (3, 1), (3, 2), (2, 0), (2, 1), (2, 2), (1, 0), (1, 1), (1, 2)]
    left = (0, 0)
    right = (0, 2)
    for number in numbers:
        if number in [1, 4, 7]:
            answer += 'L'
            left = board[number]

        elif number in [3, 6, 9]:
            answer += 'R'
            right = board[number]

        else:
            if nexthand(left, right, board[number], hand) == 'right':
                answer += 'R'
                right = board[number]
            else:
                answer += 'L'
                left = board[number]

    return answer


print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], 'right'))