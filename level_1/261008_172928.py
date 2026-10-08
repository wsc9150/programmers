# 공원 산책

def solution(park, routes):
    answer = []
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    x, y = 0, 0
    for i in range(len(park)):
        for j in range(len(park[i])):
            if park[i][j] == 'S':
                x, y = i, j
                break
    
    for route in routes:
        op, n = route.split()
        n = int(n)
        route_path = []
        
        if op == 'N':
            nx = x - n
            ny = y
            route_path = list(range(x, nx - 1, -1))
        elif op == 'S':
            nx = x + n
            ny = y
            route_path = list(range(x, nx + 1))
        elif op == 'W':
            nx = x
            ny = y - n
            route_path = list(range(y, ny - 1, -1))
        elif op == 'E':
            nx = x
            ny = y + n
            route_path = list(range(y, ny + 1))
        
        if nx < 0 or nx >= len(park) or ny < 0 or ny >= len(park[0]):
            continue
        
        is_flag = True
        if y == ny:
            for i in route_path:
                if park[i][ny] == 'X':
                    is_flag = False
                    break
        else:
            for i in route_path:
                if park[nx][i] == 'X':
                    is_flag = False
                    break
        
        if not is_flag:
            continue
        
        x, y = nx, ny
    
    answer = [x, y]
    return answer

print(solution(["SOO","OOO","OOO"], ["E 2","S 2","W 1"]))
print(solution(["SOO","OXX","OOO"], ["E 2","S 2","W 1"]))
print(solution(["OSO","OOO","OXO","OOO"], ["E 2","S 3","W 1"]))