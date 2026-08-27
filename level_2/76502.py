# 괄호 회전하기

def is_good_string(s):
    stack = []
    
    for i in s:
        if len(stack) == 0:
            stack.append(i)
        else:
            last_i = stack[-1]
            
            if last_i == '(' and i == ')':
                stack.pop()
            elif last_i == '[' and i == ']':
                stack.pop()
            elif last_i == '{' and i == '}':
                stack.pop()
            else:
                stack.append(i)
    
    if len(stack) == 0:
        return True
    
    return False

def solution(s):
    answer = 0
    idx_cnt = 0
    
    while idx_cnt < len(s):
        result = is_good_string(s)
        
        if result:
            answer += 1
        
        s = s[1:] + s[0]
        idx_cnt += 1
    
    return answer

print(solution("[](){}"))
print(solution("}]()[{"))
print(solution("[)(]"))
print(solution("}}}"))