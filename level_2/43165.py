# 타겟 넘버

answer = 0

def dfs(numbers, target, num_list, idx):
    global answer
    
    if len(num_list) == len(numbers):
        if sum(num_list) == target:
            answer += 1
        return
    
    num_list.append(numbers[idx])
    dfs(numbers, target, num_list, idx + 1)
    
    num_list.pop()
    num_list.append(-numbers[idx])
    dfs(numbers, target, num_list, idx + 1)
    
    num_list.pop()

def solution(numbers, target):
    dfs(numbers, target, [], 0)
    return answer

print(solution([1, 1, 1, 1, 1], 3))
# print(solution([4, 1, 2, 1], 4))