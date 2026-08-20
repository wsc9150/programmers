# 정수 내림차순으로 배치하기

def solution(n):
    answer = 0
    value_list = list(str(n))
    value_list.sort(reverse=True)
    answer = int(''.join(value_list))
    return answer

print(solution(118372))