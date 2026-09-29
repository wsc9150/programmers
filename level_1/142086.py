# 가장 가까운 같은 글자

def solution(s):
    answer = []
    
    index_info = {}
    
    for i in range(len(s)):
        if s[i] not in index_info:
            index_info[s[i]] = i
            answer.append(-1)
        else:
            answer.append(i - index_info[s[i]])
            index_info[s[i]] = i
    
    return answer

print(solution("banana"))
print(solution("foobar"))