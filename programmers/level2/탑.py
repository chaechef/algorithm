def solution(heights):
    answer = [0]
    heightest = heights[0]
    receive = 0
    for i in range(1, len(heights)):
        if heightest < heights[i]:
            receive = 0
            heightest= heights[i]

        if heights[i-1] > heights[i]:
            receive = i

        answer.append(receive)
    return answer

if __name__ == '__main__':
    solution([3,9,9,3,5,7,2])