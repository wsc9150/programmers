# 마법의 엘리베이터

entire_cnt = []

def dfs(number, direct, result):
    if number < 10:
        if number <= 5:
            result += number
        else:
            result += 10 - number + 1
            
        entire_cnt.append(result)
        
        return
    
    value = number % 10
    
    if direct == 'up':
        result += 10 - value
        number += 10 - value
        number = number / 10
    else:
        result += value
        number -= value
        number = number / 10
    
    dfs(number, 'up', result)
    dfs(number, 'down', result)

def solution(storey):
    answer = 0
    dfs(storey, 'up', 0)
    dfs(storey, 'down', 0)
    
    answer = min(entire_cnt)
    
    return answer

# print(solution(16))
print(solution(2554))