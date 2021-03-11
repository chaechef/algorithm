from itertools import combinations

if __name__ == "__main__":
    arr = [123,345,332,123]
    combi = combinations(arr, 2)
    for val in combi:
        print(val)
