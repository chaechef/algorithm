# def t(string):
#     return "".join(['#' if c == '1' else ' ' for c in string])
# def solution(n, arr1, arr2):
#     answer = [a | b for a, b in zip(arr1, arr2)]
#     binarr = list(map(lambda x: bin(x)[2:].zfill(n), answer))
#     ret = [t(val) for val in binarr]
#     return ret

# --

def solution(n, arr1, arr2):
    arr1, arr2 = [bin(val)[2:].rjust(n,'0') for val in arr1], [bin(val)[2:].rjust(n, '0') for val in arr2]
    ret = [[str(int(aa)|int(bb)) for aa, bb in zip(a,b)] for a, b in zip(arr1, arr2)]
    ret = ["".join(arr).replace("1", "#").replace('0', " ") for arr in ret]
    return ret

if __name__ == '__main__':
    solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28])