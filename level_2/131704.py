# 택배상자

def solution(order):
    answer = 0
    box = list(range(len(order), 0, -1))
    stack = []
    order_idx = 0
    
    while order_idx < len(order):
        if box and box[-1] == order[order_idx]:
            box.pop()
            answer += 1
            order_idx += 1
        else:
            if stack and stack[-1] == order[order_idx]:
                stack.pop()
                answer += 1
                order_idx += 1
            else:
                if box:
                    stack.append(box.pop())
                else:
                    break
    
    return answer

print(solution([4, 3, 1, 2, 5]))
print(solution([5, 4, 3, 2, 1]))