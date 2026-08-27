# 문자열 내 p와 y의 개수

from collections import Counter

def solution(s):
    answer = False
    
    s_counter = Counter(s.lower())
    if s_counter['p'] == s_counter['y']:
        answer = True
    
    return answer

print(solution("pPoooyY"))
print(solution("Pyy"))