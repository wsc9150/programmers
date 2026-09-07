# 약수의 개수와 덧셈

def find_count(n):
    value_list = [i for i in range(1, n // 2 + 1) if n % i == 0]
    return len(value_list) + 1

def solution(left, right):
    answer = 0
    
    for n in range(left, right + 1):
        count = find_count(n)
        if count % 2 == 0:
            answer += n
        else:
            answer -= n
    
    return answer

print(solution(13, 17))
print(solution(24, 27))