# 프로세스

from collections import deque

def solution(priorities, location):
    answer = 0
    process_idx = -1
    
    process_list = [(p, idx) for idx, p in enumerate(priorities)]
    process_queue = deque(process_list)
    
    while process_idx != location:
        max_priority = max(process_queue)[0]
        
        if process_queue[0][0] == max_priority:
            process_idx = process_queue.popleft()[1]
            answer += 1
        else:
            process_queue.rotate(-1)
        
    return answer

print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))