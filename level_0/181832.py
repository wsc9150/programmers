# 정수를 나선형으로 배치하기

# 첫 풀이
def solution1(n):
    answer = [[]]
    
    answer = [ [ 0 for j in range(i * n + 1, i * n + (n + 1)) ] for i in range(n) ]
    arr = [ [ j for j in range(i * n + 1, i * n + (n + 1)) ] for i in range(n) ]
    
    row = 0
    col = 0
    new_row = 0
    new_col = 0
    
    direct_list = ['r', 'd', 'l', 'u']
    direct_idx = 0
    direct = direct_list[direct_idx]
    rot_cnt = 0
    max_rot = n - 1
    change_cnt = 0
    max_change_cnt = 3
    
    while row < n and col < n:
        answer[new_row][new_col] = arr[row][col]
        
        # 정답 행렬 index 규칙
        # match direct: # match 함수는 python 버전 3.10 이상에서 쓰라고 한다.
        #     case 'u':
        #         new_row -= 1
        #     case 'd':
        #         new_row += 1
        #     case 'l':
        #         new_col -= 1
        #     case 'r':
        #         new_col += 1

        if direct == 'u':
            new_row -= 1
        elif direct == 'd':
            new_row += 1
        elif direct == 'l':
            new_col -= 1
        elif direct == 'r':
            new_col += 1

        rot_cnt += 1
        if rot_cnt == max_rot:
            direct_idx = (direct_idx + 1) % 4
            direct = direct_list[direct_idx]
            rot_cnt = 0
            change_cnt += 1
            
            if change_cnt == max_change_cnt:
                change_cnt = 0
                if max_rot == n - 1:
                    max_change_cnt -= 1

                max_rot -= 1
        
        # 원본 행렬 index 규칙
        col += 1
        if col % n == 0:
            row += 1
            col = 0
            
    return answer

# 두번째 풀이 (간결화)
def solution2(n):
    answer = [[0 for _ in range(n)] for _ in range(n)]
    
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    row = 0
    col = 0
    direct_idx = 0
    
    for i in range(1, n * n + 1):
        answer[row][col] = i
        
        new_row = row + dx[direct_idx]
        new_col = col + dy[direct_idx]
        
        # 방향 전환 조건
        if new_row < 0 or new_row >= n or new_col < 0 or new_col >= n:
            direct_idx = (direct_idx + 1) % 4
        elif answer[new_row][new_col] != 0:
            direct_idx = (direct_idx + 1) % 4
        
        row += dx[direct_idx]
        col += dy[direct_idx]
        
    return answer

# print(solution1(4))
# print(solution1(5))
print(solution2(4))
print(solution2(5))