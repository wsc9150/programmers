# JadenCase 문자열 만들기

def solution(s):
    answer = ''
    prev = ' '
    
    for i in s:
        if prev == ' ':
            answer += i.upper()
        else :
            answer += i.lower()
        
        prev = i
    
    return answer

print(solution("3people unFollowed me"))
print(solution("for the last week"))