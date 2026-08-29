# 없는 숫자 더하기

def solution(numbers):
    answer = -1
    
    answer = sum([i for i in range(10) if i not in numbers])
    
    return answer

print(solution([1,2,3,4,6,7,8,0]))
print(solution([5,8,4,0,6,7,9]))