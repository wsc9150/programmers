# 푸드 파이트 대회

def solution(food):
    answer = ''
    
    food_line = ''.join([(str(idx) * (f // 2)) for idx, f in enumerate(food[1:], 1)])
    answer = food_line + '0' + food_line[::-1]
    
    return answer

print(solution([1, 3, 4, 6]))
print(solution([1, 7, 1, 2]))