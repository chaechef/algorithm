def solution(arr1, arr2):
   answer = [[a+b for a, b in zip(arr1[i], arr2[i])] for i in range(len(arr1))]
   return answer

if __name__ == '__main__':
    solution([[1,2],[2,3]], [[3,4],[5,6]])