# H-Index

def solution(citations):
    answer = 0
    
    for i in range(max(citations), 0, -1):
        value_list = [j for j in citations if j >= i]
        if len(value_list) >= i:
            answer = i
            break
    
    return answer

print(solution([3, 0, 6, 1, 5]))