# 두 정수 사이의 합

def solution(a, b):
    answer = 0
    
    value_list = list(range(min(a, b), max(a, b) + 1))
    answer = sum(value_list)
    
    return answer

print(solution(3, 5))
print(solution(3, 3))
print(solution(5, 3))
