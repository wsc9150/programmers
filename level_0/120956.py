# 옹알이 (1)

def solution(babbling):
    answer = 0
    
    can_speak = ["aya", "ye", "woo", "ma"]
    
    for babble in babbling:
        for s in can_speak:
            babble = babble.replace(s, ' ' * len(s))
        
        if len(babble.strip()) == 0:
            answer += 1
    
    return answer

print(solution(["aya", "yee", "u", "maa", "wyeoo"]))
print(solution(["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]))