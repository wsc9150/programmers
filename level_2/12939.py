# 최댓값과 최솟값

def solution(s):
    answer = ''
    
    # value_list = [ int(i) for i in s.split(' ') ]
    # value_list = list(map(int, s.split()))
    value_list = list(map(lambda x: int(x), s.split()))
    
    answer = str(min(value_list)) + ' ' + str(max(value_list))
    
    return answer

print(solution("1 2 3 4"))
print(solution("-1 -2 -3 -4"))
print(solution("-1 -1"))
