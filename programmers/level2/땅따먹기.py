def solution(land):
    dp = [0] * 4
    for col in land:
        temp = [0] * 4
        for i in range(4):
            temp[i] = col[i] + max([dp[j] for j in range(4) if j != i])
        dp = temp
    return max(dp)

solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]])