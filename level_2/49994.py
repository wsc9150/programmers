# 방문 길이

import copy

def solution(dirs):
    answer = 0
    path = []
    current_pos = [0, 0]
    
    for d in dirs:
        prev_pos = copy.deepcopy(current_pos)
        
        if d == 'U':
            if current_pos[1] + 1 <= 5:
                current_pos[1] += 1
                if [prev_pos, d] not in path and [current_pos, 'D'] not in path:
                    path.append([prev_pos, d])
                    answer += 1
        elif d == 'D':
            if current_pos[1] - 1 >= -5:
                current_pos[1] -= 1
                if [prev_pos, d] not in path and [current_pos, 'U'] not in path:
                    path.append([prev_pos, d])
                    answer += 1
        elif d == 'R':
            if current_pos[0] + 1 <= 5:
                current_pos[0] += 1
                if [prev_pos, d] not in path and [current_pos, 'L'] not in path:
                    path.append([prev_pos, d])
                    answer += 1
        elif d == 'L':
            if current_pos[0] - 1 >= -5:
                current_pos[0] -= 1
                if [prev_pos, d] not in path and [current_pos, 'R'] not in path:
                    path.append([prev_pos, d])
                    answer += 1

    return answer

print(solution("ULURRDLLU"))
print(solution("LULLLLLLU"))