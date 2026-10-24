# 약수 구하기

def solution(n):
    answer = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            answer.append(i)
    
    temp_list = []
    if answer[-1] ** 2 == n:
        for i in range(len(answer) - 2, -1, -1):
            temp_list.append(n // answer[i])
    else:
        for i in range(len(answer) - 1, -1, -1):
            temp_list.append(n // answer[i])
    
    answer += temp_list
    return answer

print(solution(24))
print(solution(29))