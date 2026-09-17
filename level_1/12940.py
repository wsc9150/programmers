# 최대공약수와 최소공배수

import math

def solution(n, m):
    answer = []
    gcd = math.gcd(n, m)
    lcd = m
    
    while True:
        if lcd % n == 0 and lcd % m == 0:
            break
        
        lcd += m
        
    answer = [gcd, lcd]
    return answer

print(solution(3, 12))
print(solution(2, 5))