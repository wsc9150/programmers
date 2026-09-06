# 튜플

def solution(s):
    answer = []
    
    tuple_list = s.lstrip('{').rstrip('}').split('},{')
    tuple_list = sorted([set(t.split(',')) for t in tuple_list], key=lambda x: len(x))
    
    prev = set()
    for t in tuple_list:
        diff = t.difference(prev)
        answer.append(int(list(diff)[0]))
        prev = t
    
    
    return answer

print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
print(solution("{{20,111},{111}}"))
print(solution("{{123}}"))
print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))