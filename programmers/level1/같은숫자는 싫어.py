def solution(arr):
    arr2 = [arr[0]]
    for i in range(1,len(arr)):
        if arr2[-1] == arr[i]:
            continue
        else:
            arr2.append(arr[i])
    return arr2

if __name__ == "__main__":
    solution([1,1,3,3,0,1,1])