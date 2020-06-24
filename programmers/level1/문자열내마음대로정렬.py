def solution(strings, n):
    return sorted(strings, key= lambda x: (x[n], x))

if __name__ == "__main__":
    solution(['sun', 'bed', 'car'], 1)