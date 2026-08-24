# 연속 부분 수열 합의 개수

def solution(elements):
    answer = 0
    acc_list = []
    
    for part in range(len(elements)):
        for i in range(len(elements)):
            if i + part <= len(elements):
                acc_list.append(sum(elements[i:i + part]))
            else:
                acc_list.append(sum(elements[i:]) + sum(elements[0:part - len(elements[i:])]))
                
    answer = len(list(set(acc_list)))
    return answer

print(solution([7,9,1,1,4]))