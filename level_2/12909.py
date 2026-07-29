# 올바른 괄호

def solution(s):
    answer = True
    
    stack = []
    for i in s:
        if len(stack) == 0:
            stack.append(i)
            continue
        
        last_element = stack.pop()
        if last_element == '(' and i == ')':
            continue
        else:
            stack.append(last_element)
            stack.append(i)
    
    if len(stack) != 0:
        answer = False
        
    return answer

print(solution("()()"))
print(solution("(())()"))
print(solution(")()("))
print(solution("(()("))
