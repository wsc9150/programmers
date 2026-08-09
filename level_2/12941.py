# 최솟값 만들기

def solution(A,B):
    answer = 0
    
    A.sort()
    B.sort(reverse=True)
    
    zip_list = list(zip(A, B))
    answer = sum([ i[0] * i[1] for i in zip_list ])
    
    return answer

print(solution([1, 4, 2], [5, 4, 4]))
print(solution([1,2], [3,4]))