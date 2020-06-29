def get_root(a,b,c):
     r1 = (-b + (b**2 - 4*a*c)**0.5) / (2*a)
     r2 = (-b - (b**2 - 4*a*c)**0.5) / (2*a)
     return map(int, (r1, r2))

def solution(brown, yellow):
    answer = []
    a, b = get_root(2, 4-brown, 2*yellow)
    return [a+2, b+2]


solution(10, 2)
solution(8, 1)
solution(24, 24)