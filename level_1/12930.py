# 이상한 문자 만들기

def solution(s):
    answer = ''
    
    word_list = []
    prev = ''
    for i in s:
        if (prev.isalpha() and i.isalpha()) or (not prev.isalpha() and not i.isalpha()):
            prev += i
        else:
            word_list.append(prev)
            prev = i
            
    word_list.append(prev)
    word_list = [word for word in word_list if word != '']
    
    new_word_list = []
    for word in word_list:
        temp_word = ''
        
        for idx, s in enumerate(word):
            if idx % 2 == 0:
                temp_word += s.upper()
            else:
                temp_word += s.lower()
        
        new_word_list.append(temp_word)
    
    answer = ''.join(new_word_list)

    return answer

print(solution("try hello world"))