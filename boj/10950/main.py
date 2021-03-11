import sys

if __name__=="__main__":
    testcase = int(sys.stdin.readline())
    for case in range(testcase):
        inputs = list(map(int,sys.stdin.readline().split()))
        print(inputs[0] + inputs[1])
