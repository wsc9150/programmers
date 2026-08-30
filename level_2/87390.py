# n^2 배열 자르기

def find_value(n, index):
    d = index // n
    r = index % n
    
    # 몫이 d라면, 행은 d + 1행 -> 그 행은 d + 1 부터 시작
    # 나머지가 r이면, 열은 r + 1열
    
    # 열 번호가 행 번호보다 크면 값은 열 번호가 되고, 작으면 행 번호가 값이 된다.
    value = r + 1 if r + 1 > d + 1 else d + 1
    return value
    
def solution(n, left, right):
    answer = []
    
    for i in range(left, right + 1):
        answer.append(find_value(n, i))
    
    return answer

print(solution(3, 2, 5))
print(solution(4, 7, 14))