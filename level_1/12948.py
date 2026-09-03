# 핸드폰 번호 가리기

def solution(phone_number):
    answer = '*' * (len(phone_number) - 4) + phone_number[-4::1]
    
    return answer

print(solution("01033334444"))
print(solution("027778888"))