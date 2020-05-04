if __name__ == "__main__":
    testcase = int(input())
    for i in range(testcase):
        line = list(map(int, input().split()))
        l = line[0]
        scores = line[1:]
        overavg = 0
        scoreavg = sum(scores) / len(scores)
        for score in scores:
            if score > scoreavg :
                overavg += 1
        print(format( overavg / l * 100, ".3f")+"%")


