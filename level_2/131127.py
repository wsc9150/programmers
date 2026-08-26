# 할인 행사

from collections import Counter

def solution(want, number, discount):
    answer = 0
    want_info = {}
    
    for i in range(len(want)):
        want_info[want[i]] = number[i]
    
    for i in range(len(discount)):
        ten_day_list = discount[i:i + 10]
        sale_info = Counter(ten_day_list)
        
        for w in want:
            if w not in sale_info.keys():
                break
                
            if want_info[w] != sale_info[w]:
                break
        else:
            answer += 1
                
    return answer

print(solution(["banana", "apple", "rice", "pork", "pot"], [3, 2, 2, 2, 1], ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]))
print(solution(["apple"], [10], ["banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana"]))
