# 같은 숫자는 싫어

def solution(arr):
    answer = []
    for a in arr:
        if len(answer) == 0:
            answer.append(a)
        
        if answer[-1] != a:
            answer.append(a)
            
    return answer

print(solution([1,1,3,3,0,1,1]))
print(solution([4,4,4,3,3]))