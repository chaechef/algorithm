import sys


if __name__ == "__main__":
    pipeline = sys.stdin.readline().strip()
    stack = []
    plen = len(pipeline)
    ans = 0
    for i in range(plen):
        if pipeline[i] == "(":
            stack.append(pipeline[i])
        else:
            #raser
            if pipeline[i-1] == "(":
                stack.pop()
                ans += len(stack)
            else:
                stack.pop()
                ans += 1

    print(ans)

