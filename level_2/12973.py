# 짝지어 제거하기

def solution(s):
    answer = -1
    
    stack = []
    
    for a in s:
        if len(stack) == 0:
            stack.append(a)
        else:
            if stack[-1] == a:
                stack.pop()
            else:
                stack.append(a)
    
    if len(stack) == 0:
        answer = 1
    else:
        answer = 0
    
    return answer

print(solution("baabaa"))
print(solution("cdcd"))