# 시저 암호

def solution(s, n):
    answer = ''
    
    for i in s:
        if i == ' ':
            answer += i
        elif 'a' <= i <= 'z':
            i_ascii = ord(i) + n
            if i_ascii > 122:
                i_ascii = i_ascii - 26
            answer += chr(i_ascii)
        else:
            i_ascii = ord(i) + n
            if i_ascii > 90:
                i_ascii = i_ascii - 26
            answer += chr(i_ascii)
    
    return answer

print(solution("AB", 1))
print(solution("z", 1))
print(solution("a B z", 4))