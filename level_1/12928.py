# 약수의 합

def solution(n):
    answer = 0
    
    value_list = [ i for i in range(1, n + 1) if n % i == 0  ]
    answer = sum(value_list)
    
    return answer

print(solution(12))
print(solution(5))