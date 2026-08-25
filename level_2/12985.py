# 예상 대진표

def solution(n,a,b):
    answer = 1
    
    while True:
        if (a + 1) // 2 == (b + 1) // 2:
            break
            
        a = (a + 1) // 2
        b = (b + 1) // 2
        
        answer += 1
        
    return answer

print(solution(8, 4, 7))