def solution(N, stages):
    slen = len(stages)
    clear = [0] * (N+1)
    nclear = [0] * (N+1)

    for val in stages:
        for i in range(1, val):
            clear[i] += 1
        if val != N+1:
            nclear[val] += 1
    ret = []
    for idx in range(1, N+1):
        if clear[idx] + nclear[idx] == 0:
           ret.append((idx, 0))
        else:
            ret.append((idx, nclear[idx] / (clear[idx] + nclear[idx])))

    return [a[0] for a in sorted(ret, key=lambda a: (-a[1],a[0]))]



if __name__ == '__main__':
    a = solution(4, [4,4,4,4,4])
    print(a)