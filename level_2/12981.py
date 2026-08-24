# 영어 끝말잇기

def solution(n, words):
    answer = []
    word_info = {}
    
    for i in range(len(words)):
        # 단어 연결이 안되는 경우
        if i > 0 and words[i - 1][-1] != words[i][0]:
            answer = [i % n + 1, i // n + 1]
            break
        
        # 중복 단어 나온 경우
        if words[i] not in word_info.keys():
            word_info[words[i]] = 1
        else:
            answer = [i % n + 1, i // n + 1]
            break
    
    if len(answer) == 0:
        answer = [0, 0]
    
    return answer

print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
print(solution(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]))
print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))