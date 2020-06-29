def solution(phone_book):
    answer = True
    s = set(phone_book)
    for phone in phone_book:
        for i in range(1, len(phone)):
            if phone[:i] in s:
                return False

    return answer


solution(['119', '97674223', '1195524421'])