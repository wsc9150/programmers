# [3차] n진수 게임

def transform(n, value):
    value_list = []
    value_info = { 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E',15: 'F', }
    
    if value < n:
        value_list.append(value)
    else:
        while value >= n:
            r = value % n
            value = value // n
            value_list.append(r)
            
        value_list.append(value)
        
    value_list = [value_info[i] if i in value_info else str(i) for i in value_list]
    value_list.reverse()
    return value_list

def solution(n, t, m, p):
    answer = ''
    num_list = []
    
    for i in range(t * m + 1):
        result = transform(n, i)
        num_list.extend(result)
    
    answer = ''.join(num_list[p - 1:t * m:m])
    
    return answer

print(solution(2, 4, 2, 1))
print(solution(16, 16, 2, 1))
print(solution(16, 16, 2, 2))