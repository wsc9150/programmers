# 멀리 뛰기

def solution(n):
    answer = 0
    step_list = [0 for _ in range(n)]
    
    step_list[0] = 1
    
    if n > 1:
        step_list[1] = 2
    
    for i in range(2, n):
        step_list[i] = step_list[i - 1] + step_list[i - 2]
    
    answer = step_list[-1] % 1234567
    
    return answer

print(solution(4))
print(solution(3))