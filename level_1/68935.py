# 3진법 뒤집기

def solution(n):
    answer = 0
    three = ''
    
    while n >= 3:
        d = n // 3
        r = n % 3
        
        three += str(r)
        n = d
    
    three += str(n)
    three = three[::-1]
    
    for i in range(len(three)):
        answer += int(three[i]) * (3 ** i)
    
    return answer

print(solution(45))
print(solution(125))