# 나누어 떨어지는 숫자 배열

def solution(arr, divisor):
    answer = sorted([i for i in arr if i % divisor == 0]) if len([i for i in arr if i % divisor == 0]) else [-1]
    
    return answer

print(solution([5, 9, 7, 10], 5))
print(solution([2, 36, 1, 3], 1))
print(solution([3,2,6], 10))