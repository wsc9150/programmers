# 평행

def solution(dots):
    answer = 0
    
    for i in range(len(dots) - 1):
        for j in range(i + 1, len(dots)):
            first_line = [dots[i], dots[j]]
            second_line = [dots[k] for k in range(len(dots)) if k not in [i, j]]
            
            first_w = (first_line[1][0] - first_line[0][0]) / (first_line[1][1] - first_line[0][1])
            second_w = (second_line[1][0] - second_line[0][0]) / (second_line[1][1] - second_line[0][1])
            
            if first_w == second_w:
                answer = 1
                break
            
    return answer

print(solution([[1, 4], [9, 2], [3, 8], [11, 6]]))
print(solution([[3, 5], [4, 1], [2, 4], [5, 10]]))