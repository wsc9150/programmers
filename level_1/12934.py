# 정수 제곱근 판별

import math

def solution(n):
    answer = 0
    value = math.sqrt(n)
    
    answer = (value + 1) ** 2 if value == int(value) else -1
    return answer

print(solution(121))
print(solution(3))