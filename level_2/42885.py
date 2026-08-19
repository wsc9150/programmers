# 구명보트

def solution(people, limit):
    answer = 0
    
    people.sort()
    start_idx = 0
    end_idx = len(people) - 1
    
    while start_idx < end_idx:
        if people[start_idx] + people[end_idx] <= limit:
            answer += 1
            start_idx += 1
            end_idx -= 1
        else:
            answer += 1
            end_idx -= 1
    
    if start_idx == end_idx:
        answer += 1
        
    return answer

print(solution([70, 50, 80, 50], 100))
print(solution([70, 80, 50], 100))