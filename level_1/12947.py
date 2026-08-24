# 하샤드 수

def solution(x):
    answer = True if x % sum([int(i) for i in str(x)]) == 0 else False
    return answer

print(solution(10))
print(solution(12))
print(solution(11))
print(solution(13))