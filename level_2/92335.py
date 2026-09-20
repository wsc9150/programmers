# k진수에서 소수 개수 구하기

def transform_number(n, k):
    transformed = ''
    
    while n > k:
        d = n // k
        r = n % k
        transformed += str(r)
        
        n = d
    
    transformed += str(n)
    return transformed[::-1]

def is_sosu(n):
    is_flag = True
    
    if n == 1:
        is_flag = False
    else:
        for i in range(2, int(n ** 0.5) + 1): # n // 2 하면 시간초과 난다.
            if n % i == 0:
                is_flag = False
                break
    
    return is_flag

def solution(n, k):
    answer = 0
    num_string = transform_number(n, k)
    split_list = num_string.split('0')
    
    if len(split_list) > 1:
        zero_list = ['0'] * (len(split_list) - 1)
        zip_list = zip(split_list, zero_list) # split 하면서 없어진 0 넣기
        
        value_list = []
        for z in zip_list:
            value_list.extend(z)
        value_list.append(split_list[-1])
        value_list = [i for i in value_list if i != ''] # 빈 문자열 제거 ('00' split하면 빈 문자열 나온다.)
    else:
        value_list = split_list
        
    if len(value_list) == 1:
        if is_sosu(int(value_list[0])):
            answer = 1
    else:
        for i in range(len(value_list)):
            value = int(value_list[i])
    
            if value != 0 and value != 1:
                if is_sosu(value):
                    if i == 0 and i + 1 < len(value_list) and value_list[i + 1] == '0': # 인덱스 만족 조건 부여
                        answer += 1
                    elif i == len(value_list) - 1 and i - 1 >= 0 and value_list[i - 1] == '0':
                        answer += 1
                    elif i + 1 < len(value_list) and i - 1 >= 0 and value_list[i - 1] == '0' and value_list[i + 1] == '0':
                        answer += 1
    
    return answer

print(solution(437674, 3))
print(solution(110011, 10))