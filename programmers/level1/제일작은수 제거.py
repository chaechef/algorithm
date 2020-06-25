def solution(arr):
    if len(arr) == 1:
        return [-1]
    arr.remove(min(arr))
    return arr

if __name__ == "__main__":
    solution([4,3,2,1])