# 두 개 뽑아서 더하기

def solution(numbers):
    answer = []
    
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i != j:
                answer.append(numbers[i] + numbers[j])
    
    return sorted(list(set(answer)))

print(solution([2,1,3,4,1]))
print(solution([5,0,2,7]))