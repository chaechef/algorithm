def solution(n):
    answer = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            answer += i + (n // i)
            if i == n // i:
                answer -= i
    return answer

if __name__ == '__main__':
    solution(25)