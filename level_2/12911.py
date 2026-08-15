# 다음 큰 숫자

def solution(n):
    answer = 0
    binary_n = bin(n)
    
    while True:
        n += 1
        
        if binary_n.count('1') == bin(n).count('1'):
            answer = n
            break
    
    return answer

print(solution(78))
print(solution(15))