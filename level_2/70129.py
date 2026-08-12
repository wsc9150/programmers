# 이진 변환 반복하기

def solution(s):
    answer = []
    cnt = 0
    zero_cnt = 0
    
    while s != '1':
        zero_cnt += s.count('0')
        none_zero_s = s.replace('0', '')
        binary_s = bin(len(none_zero_s)).replace('0b', '')
        
        cnt += 1
        s = binary_s
    
    answer = [cnt, zero_cnt]
    return answer

print(solution("110010101001"))
print(solution("01110"))
print(solution("1111111"))
