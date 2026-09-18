# 최소직사각형

def solution(sizes):
    answer = 0
    
    sizes = [[size[0], size[1]] if size[0] > size[1] else [size[1], size[0]] for size in sizes]
    sizes_t = list(zip(*sizes))
    answer = max(sizes_t[0]) * max(sizes_t[1])
    
    return answer

print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))
print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))
print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]))