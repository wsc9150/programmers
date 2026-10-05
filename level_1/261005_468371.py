# 노란불 신호등

def solution(signals):
    answer = 0
    signal_list = []
    
    for signal in signals:
        temp = []
        for idx, s in enumerate(signal):
            temp += [idx] * s
        signal_list.append(temp * 1000000)
    
    min_len = min([len(i) for i in signal_list])
    for i in range(min_len):
        for signal in signal_list:
            if signal[i] != 1:
                break
        else:
            answer = i + 1
            break
    
    if answer == 0:
        answer = -1
    return answer

print(solution([[2, 1, 2], [5, 1, 1]]))
print(solution([[2, 3, 2], [3, 1, 3], [2, 1, 1]]))
print(solution([[3, 3, 3], [5, 4, 2], [2, 1, 2]]))
print(solution([[1, 1, 4], [2, 1, 3], [3, 1, 2], [4, 1, 1]]))