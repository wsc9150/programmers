# 2 x n 타일링

def solution(n):
    answer = 0
    
    if n == 1:
        answer = 1
    elif n == 2:
        answer = 2
    else:
        prev = 2
        prev_prev = 1
        
        for i in range(n - 2):
            answer = prev + prev_prev
            prev_prev = prev
            prev = answer
    
    return answer % 1000000007

print(solution(4))