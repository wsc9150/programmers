# 서울에서 김서방 찾기

def solution(seoul):
    answer = ''
    
    kim_idx = seoul.index('Kim')
    
    return f'김서방은 {kim_idx}에 있다'

print(solution(["Jane", "Kim"]))