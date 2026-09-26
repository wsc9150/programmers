# 숫자 변환하기

from collections import deque

def solution(x, y, n):
    answer = 0
    cnt_list = []
    q = deque([[y, 0]])
    visited = [False] * (y + 1)
    
    while q:
        y, cnt = q.popleft()
        
        if not visited[y]:
            visited[y] = True
        else:
            continue
        
        if y < x:
            continue
        
        if y == x:
            cnt_list.append(cnt)
        else:
            if y % 3 == 0:
                q.append([y // 3, cnt + 1])
            if y % 2 == 0:
                q.append([y // 2, cnt + 1])
            
            q.append([y - n, cnt + 1])
            
    answer = min(cnt_list) if cnt_list else -1
    return answer

print(solution(10, 40, 5))
print(solution(10, 40, 30))
print(solution(2, 5, 4))