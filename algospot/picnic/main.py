import sys

def recursion(havefriends, isfriend):
    smallest = 0
    for i, v in enumerate(havefriends):
        if v == 0:
            smallest = i
            break;
    else:
        return 1;

    ret = 0
    for idx in range(smallest+1, sn):
        if isfriend[smallest][idx] == 1 and havefriends[idx] == 0:
            havefriends[smallest] = havefriends[idx] = 1
            ret += recursion(havefriends, isfriend)
            havefriends[smallest] = havefriends[idx] = 0

    return ret


if __name__ == "__main__":
    for _ in range(int(sys.stdin.readline())):
        sn, cb = map(int, sys.stdin.readline().strip().split())
        isfriend = [[0 for _ in range(sn)] for _ in range(sn)]
        friends = list(map(int, sys.stdin.readline().strip().split()))
        for a, b in zip(friends[::2], friends[1::2]):
            isfriend[a][b], isfriend[b][a] = 1, 1
        havefriends = [0] * sn
        res = recursion(havefriends, isfriend)
        print(res)


