# 뒤에 있는 큰 수 찾기

def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []
    
    numbers = [(i, numbers[i]) for i in range(len(numbers))]
    
    for item in numbers:
        if len(stack) == 0:
            stack.append(item)
        else:
            while len(stack) > 0:
                if stack[-1][1] < item[1]:
                    answer[stack[-1][0]] = item[1]
                    stack.pop()
                else:
                    break
            
            stack.append(item)
    
    return answer

print(solution([2, 3, 3, 5]))
print(solution([9, 1, 5, 3, 6, 2]))