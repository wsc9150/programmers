# 내적

def solution(a, b):
    answer = 1234567890
    
    zip_list = list(zip(a, b))
    dot_list = [i[0] * i[1] for i in zip_list]
    answer = sum(dot_list)
    
    return answer

print(solution([1,2,3,4], [-3,-1,0,2]))
print(solution([-1,0,1], [1,0,-1]))