# 귤 고르기

def solution(k, tangerine):
    answer = 0
    tangerine_dict = {}
    
    for t in tangerine:
        if t not in tangerine_dict.keys():
            tangerine_dict[t] = 1
        else:
            tangerine_dict[t] += 1
    
    tangerine_list = list(tangerine_dict.items())
    tangerine_list.sort(key=lambda x: -x[1])
    # print(tangerine_list)
    
    acc_value = 0
    for size, cnt in tangerine_list:
        acc_value += cnt
        answer += 1
        
        if acc_value >= k:
            break
    
    return answer

print(solution(6, [1, 3, 2, 5, 4, 5, 2, 3]))
print(solution(4, [1, 3, 2, 5, 4, 5, 2, 3]))
print(solution(2, [1, 1, 1, 1, 2, 2, 2, 3]))