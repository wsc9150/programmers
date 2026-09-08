# [1차] 뉴스 클러스터링

import re, math

def solution(str1, str2):
    answer = 0
    
    str1 = str1.lower()
    str2 = str2.lower()
    
    sep_str1 = [str1[i:i + 2] for i in range(len(str1) - 1) if len(re.sub(r'[a-zA-Z]', '', str1[i:i + 2])) == 0]
    sep_str2 = [str2[i:i + 2] for i in range(len(str2) - 1) if len(re.sub(r'[a-zA-Z]', '', str2[i:i + 2])) == 0]
    
    len_str1 = len(sep_str1)
    len_str2 = len(sep_str2)
    
    inter = 0
    for s1 in sep_str1:
        if s1 in sep_str2:
            inter += 1
            sep_str2.pop(sep_str2.index(s1))
    
    union = len_str1 + len_str2 - inter
    
    if union == 0 and inter == 0:
        answer = 65536
    else:
        answer = math.floor(inter / union * 65536)
    
    return answer

print(solution("FRANCE", "french"))
print(solution("handshake", "shake hands"))
print(solution("aa1+aa2", "AAAA12"))
print(solution("E=M*C^2", "e=m*c^2"))