# N개의 최소공배수

def solution(arr):
    answer = 0
    max_value = max(arr)
    lcm = max_value
    
    while True:
        rest_list = [lcm % i == 0 for i in arr]
        if all(rest_list):
            break
            
        lcm += max_value
    
    return lcm

print(solution([2,6,8,14]))
print(solution([1,2,3]))