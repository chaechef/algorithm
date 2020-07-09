def solution(arr):
    answer = [val for idx, val in enumerate(arr) if val != arr[idx-1] or idx == 0]
    return answer

if __name__ == "__main__":
    solution([1,1,3,3,0,1,1])