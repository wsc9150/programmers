# 땅따먹기

def solution(land):
    answer = 0
    
    for i in range(1, len(land)):
        for j in range(4):
            land[i][j] = land[i][j] + max([land[i - 1][p] for p in range(4) if p != j])
    
    answer = max(land[-1])

    return answer

print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]))