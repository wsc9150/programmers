# 게임 맵 최단거리

from collections import deque

def solution(maps):
    answer = 0
    q = deque([(0, 0)])
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    height = len(maps)
    width = len(maps[0])
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= height or ny < 0 or ny >= width:
                continue
            
            if maps[nx][ny] == 0:
                continue
            
            if maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                q.append((nx, ny))
    
    answer = -1 if maps[height - 1][width - 1] == 1 else maps[height - 1][width - 1]
    return answer

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))