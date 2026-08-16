# 피보나치 수

def solution(n):
    answer = 0
    
    value_list = [0 for i in range(n + 1)]
    value_list[1] = 1
    
    for i in range(2, len(value_list)):
        value_list[i] = value_list[i - 1] + value_list[i - 2]
    
    answer = value_list[n] % 1234567
    return answer

print(solution(3))
print(solution(5))