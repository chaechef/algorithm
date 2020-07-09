def solution(N, stages):
    cleared = [0] * (N + 1)
    now = [0] * (N + 1)

    for stage in stages:
        if stage != N + 1:
            now[stage] += 1
        for i in range(1, stage):
            cleared[i] += 1

    failrate = [(now[idx] / (now[idx] + cleared[idx]), idx) if now[idx] + cleared[idx] != 0 else (0, idx) for idx in range(1, N + 1)]
    failrate.sort(key=lambda a: (-a[0], a[1]))
    return list(map(lambda a: a[1] ,failrate))


if __name__ == '__main__':
    a = solution(5, [2, 1, 2, 6, 2, 4, 3, 3])
    print(a)
