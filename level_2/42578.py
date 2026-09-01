# 의상

def solution(clothes):
    answer = 1
    clothes_info = {}
    
    for c in clothes:
        if c[1] not in clothes_info.keys():
            clothes_info[c[1]] = 2 # '아무것도 착용 안함'도 처음에 같이 포함
        else:
            clothes_info[c[1]] += 1
    
    value_list = [i[1] for i in clothes_info.items()]
    for value in value_list:
        answer *= value
                
    return answer - 1 # 모든 종류 착용 안한 경우의 수를 빼기

print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))