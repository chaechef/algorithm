if __name__ == "__main__":
    testCase = int(input())
    for i in range(testCase):
        temp = list(map(int, input().split()))
        print(f'Case #{i+1}: {temp[0]+temp[1]}')
