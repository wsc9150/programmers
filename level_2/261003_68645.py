# 삼각 달팽이

def solution(n):
    answer = [[0] * i for i in range(1, n + 1)]
    dx = [1, 0, -1]
    dy = [0, 1, -1]
    
    x, y = 0, 0
    direct_idx = 0
    end = sum([i for i in range(n + 1)])
    
    for i in range(1, end + 1):
        answer[x][y] = i
        
        next_x = x + dx[direct_idx]
        next_y = y + dy[direct_idx]
        
        if next_x < 0 or next_x >= n or next_y < 0 or next_y >= n or answer[next_x][next_y] != 0:
            direct_idx = (direct_idx + 1) % 3
            
            next_x = x + dx[direct_idx]
            next_y = y + dy[direct_idx]
        
        x = next_x
        y = next_y
    
    temp = []
    for i in answer:
        temp += i
    
    return temp

print(solution(4))
print(solution(5))
print(solution(6))