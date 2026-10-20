# 숫자 문자열과 영단어

def solution(s):
    answer = 0
    number_info = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
    }
    
    num_str = ''
    num_eng = ''
    for i in s:
        if i.isdigit():
            num_str += i
        else:
            num_eng += i
            if num_eng in number_info:
                num_str += number_info[num_eng]
                num_eng = ''
    
    answer = int(num_str)
    return answer

print(solution("one4seveneight"))
print(solution("23four5six7"))
print(solution("2three45sixseven"))
print(solution("123"))