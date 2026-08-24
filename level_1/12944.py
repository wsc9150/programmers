# 평균 구하기

def solution(arr):
    # answer = sum([i / len(arr) for i in arr])
    answer = sum(arr) / len(arr)
    return answer

print(solution([1,2,3,4]))
print(solution([5,5]))