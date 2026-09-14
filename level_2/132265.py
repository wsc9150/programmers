# 롤케이크 자르기

from collections import Counter

def solution(topping):
    answer = 0
    
    topping_counter = Counter(topping)
    me_set = set()
    
    for t in topping:
        me_set.add(t)
        topping_counter[t] -= 1
        if topping_counter[t] == 0:
            topping_counter.pop(t)
        
        if len(me_set) == len(topping_counter):
            answer += 1
    
    return answer

print(solution([1, 2, 1, 3, 1, 4, 1, 2]))
print(solution([1, 2, 3, 1, 4]))