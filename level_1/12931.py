# 자릿수 더하기

def solution(n):
    answer = 0
    
    value_list = list(str(n))
    answer = sum([int(i) for i in value_list])

    return answer

print(solution(123))
print(solution(987))