# 숫자의 표현

def solution(n):
    answer = 0
    value_list = [i for i in range(1, n + 1)]
    
    acc_sum = 0
    start_idx = 0
    
    while True:
        for i in range(start_idx, n):
            acc_sum += value_list[i]
            
            if acc_sum == n:
                answer += 1
                break
            
            if acc_sum > n:
                break
        
        acc_sum = 0
        start_idx += 1
        
        if start_idx >= n:
            break
        
        if value_list[start_idx] >= (n // 2 + 1):
            answer += 1
            break
    
    return answer

print(solution(15))