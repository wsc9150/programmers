# 음양 더하기

def solution(absolutes, signs):
    answer = 123456789
    
    value_list = [absolutes[i] if signs[i] else -absolutes[i] for i in range(len(absolutes))]
    answer = sum(value_list)
    
    return answer

print(solution([4,7,12], [True,False,True]))
print(solution([1,2,3], [False,False,True]))