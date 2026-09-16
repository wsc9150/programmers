# 주식가격

def solution(prices):
    answer = [0] * len(prices)
    stack = []
    
    for i in range(len(prices)):
        if not stack:
            stack.append(i)
        else:
            for idx in stack:
                answer[idx] += 1
            
            while stack:
                if prices[stack[-1]] > prices[i]:
                    stack.pop()
                else:
                    break
            
            stack.append(i)
    
    return answer

print(solution([1, 2, 3, 2, 3]))