# 짝수와 홀수

def solution(num):
    answer = 'Even' if num % 2 == 0 else 'Odd'
    return answer

print(solution(3))
print(solution(4))