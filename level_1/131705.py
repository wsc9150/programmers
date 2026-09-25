# 삼총사

from itertools import combinations

def solution(number):
    answer = 0
    
    comb_list = list(combinations(number, 3))
    
    for c in comb_list:
        if sum(c) == 0:
            answer += 1
    
    return answer

print(solution([-2, 3, 0, 2, -5]))
print(solution([-3, -2, -1, 0, 1, 2, 3]))
print(solution([-1, 1, -1, 1]))