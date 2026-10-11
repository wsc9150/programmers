# 콜라 문제

def solution(a, b, n):
    answer = 0
    
    while n >= a:
        d = (n // a) * b
        r = n % a
        
        answer += d
        n = d + r
    
    return answer

print(solution(2, 1, 20))
print(solution(3, 1, 20))