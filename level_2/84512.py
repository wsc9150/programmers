# 모음사전

answer = 0
is_flag = False

def dfs(word_seq, word):
    global answer, is_flag
    
    if len(word_seq) == 5:
        return word_seq
    
    alpha_list = ['A', 'E', 'I', 'O', 'U']
    
    for a in alpha_list:
        word_seq.append(a)
        
        if not is_flag:
            answer += 1
        
        if ''.join(word_seq) == word:
            is_flag = True
        
        word_seq = dfs(word_seq, word)
        word_seq.pop()
        
    return word_seq
        
def solution(word):
    global answer
    word_seq = []
    
    result = dfs(word_seq, word)
    return answer

print(solution("AAAAE"))
# print(solution("AAAE"))
# print(solution("I"))
# print(solution("EIO"))