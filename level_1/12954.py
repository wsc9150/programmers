# x만큼 간격이 있는 n개의 숫자

def solution(x, n):
    if x == 0:
        answer = [0] * n
    else:
        answer = [i for i in range(x, x * n + (1 if x >= 0 else -1), x)]
        
    return answer

print(solution(2, 5))
print(solution(4, 3))
print(solution(-4, 2))