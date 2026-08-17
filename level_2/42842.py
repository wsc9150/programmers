# 카펫

def solution(brown, yellow):
    answer = []
    brown_list = []
    
    for i in range(1, yellow + 1):
        if yellow % i == 0:
            height = i
            width = yellow // i
            
            # 효율성 증가를 위한 반복문 break
            if height > width:
                break
            
            grid = height * 2 + width * 2 + 4
            
            brown_list.append((width, height, grid))
    
    carpet = [i for i in brown_list if i[2] == brown][0]
    answer = [carpet[0] + 2, carpet[1] + 2]
    
    return answer

print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))