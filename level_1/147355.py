# 크기가 작은 부분 문자열

def solution(t, p):
    answer = len([t[i:i + len(p)] for i in range(len(t) - len(p) + 1) if t[i:i + len(p)] <= p])
    return answer

print(solution("3141592", "271"))
print(solution("500220839878", "7"))
print(solution("10203", "15"))