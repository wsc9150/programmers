# 제일 작은 수 제거하기

def solution(arr):
    answer = []
    min_value = min(arr)
    arr = [i for i in arr if i > min_value]
    answer = arr if len(arr) > 0 else [-1]
    return answer

print(solution([4,3,2,1]))
print(solution([10]))