# 피로도

from itertools import permutations

def solution(k, dungeons):
    answer_list = []
    dungeon_list = list(permutations(dungeons))
    
    for dungeon in dungeon_list:
        answer = 0
        tired = k
        
        for need, consume in dungeon:
            if tired >= need:
                tired -= consume
                answer += 1
        
        answer_list.append(answer)
    
    return max(answer_list)

print(solution(8, [[80,20],[50,40],[30,10]]))