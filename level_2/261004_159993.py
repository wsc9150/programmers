# 미로 탈출

from collections import deque
import copy

def solution(maps):
    answer = 0
    q = deque()
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    maps = [list(i) for i in maps]
    find_lever_map = copy.deepcopy(maps)
    
    x, y = 0, 0
    end_x, end_y = 0, 0
    lever_x, lever_y = 0, 0
    for i in range(len(maps)):
        for j in range(len(maps[i])):
            if maps[i][j] == 'S':
                x, y = i, j
            
            if maps[i][j] == 'E':
                end_x, end_y = i, j
            
            if maps[i][j] == 'L':
                lever_x, lever_y = i, j
    
    is_lever = False
    find_lever_map[x][y] = 0
    q.append((x, y))
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
        
            if nx < 0 or nx >= len(maps) or ny < 0 or ny >= len(maps[0]):
                continue

            if find_lever_map[nx][ny] == 'X' or type(find_lever_map[nx][ny]) == int:
                continue
            
            if find_lever_map[nx][ny] == 'L':
                is_lever = True
                maps[nx][ny] = find_lever_map[x][y] + 1
                x = nx
                y = ny
                break
            
            find_lever_map[nx][ny] = find_lever_map[x][y] + 1
            q.append((nx, ny))
        
        if is_lever:
            break
    
    # 위에서 레버 위치를 찾지 못하고 반복이 끝난 경우
    # 여기서 빠지지 않고 아래로 내려가면 string + 1 의 연산이 이루어지기 때문에 에러가 발생한다.
    if x != lever_x or y != lever_y:
        return -1
    
    q = deque()
    q.append((x, y))
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= len(maps) or ny < 0 or ny >= len(maps[0]):
                continue

            if maps[nx][ny] == 'X' or type(maps[nx][ny]) == int:
                continue
            
            maps[nx][ny] = maps[x][y] + 1
            q.append((nx, ny))
    
    answer = maps[end_x][end_y] if type(maps[end_x][end_y]) == int else -1
        
    return answer

print(solution(["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]))
print(solution(["LOOXS","OOOOX","OOOOO","OOOOO","EOOOO"]))