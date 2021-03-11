import sys
sys.setrecursionlimit(10**9)

input = sys.stdin.readline

signal = [
    "1110000000000000",
    "0001000101010000",
    "0000100000100011",
    "1000111100000000",
    "0000001110101000",
    "1010000000000011",
    "0001000000000011",
    "0000110100000011",
    "0111110000000000",
    "0001110001000100",
]



def recursion(index, count):
    global mincount
    if index == 10:
        return 0

    for i in range(4):
        for idx, val in enumerate(signal[index]):
            if val == "1":
                clocks[idx] += 3 * i
                if clocks[idx] > 12:
                    clocks[idx] -= 12

        if clocks.count(12) == 16 and mincount > count + i:
            mincount = count + i

        recursion(index+1, count + i)

        for idx, val in enumerate(signal[index]):
            if val == "1":
                clocks[idx] -= 3 * i
                if clocks[idx] < 3:
                    clocks[idx] += 12


if __name__ == "__main__":
    for _ in range(int(input())):
        clocks = list(map(int, input().strip().split()))
        mincount = 10 ** 9
        recursion(0, 0)
        if mincount == 10 ** 9:
            print(-1)
        else:
            print(mincount)