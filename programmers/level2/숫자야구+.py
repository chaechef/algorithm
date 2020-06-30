from itertools import permutations, combinations

def solution(baseball):
    nums = list(range(1,10))
    permu = list(permutations(nums, 3))

    for query in baseball:
        n, s, b = query
        s1, s2, s3 = map(int, str(n))
        if s == 1:
            permu = [val for val in permu if val[0] == s1 or val[1] == s2 or val[2] == s3]
        if s == 2:
            permu = [val for val in permu
                     if (val[0] == s1 and val[1] == s2) or
                        (val[0] == s1 and val[2] == s3) or
                        (val[1] == s2 and val[2] == s3)]
        if s == 3:
            return 1

        if b == 1:
            permu = [val for val in permu if val[0] != s1 and val[1] != s2]

        print(permu)

    return len(permu)


solution([[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]])