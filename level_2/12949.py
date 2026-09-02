# 행렬의 곱셈

def solution(arr1, arr2):
    answer = []
    transformed_arr2 = []
    
    # arr2 전치
    for i in range(len(arr2[0])):
        temp_arr = []
        for j in range(len(arr2)):
            temp_arr.append(arr2[j][i])
        
        transformed_arr2.append(temp_arr)
    
    # 배열 곱 연산 수행
    for a1 in arr1:
        temp_arr = []
        for a2 in transformed_arr2:
            sum_value = 0
            for i in range(len(a1)):
                sum_value += a1[i] * a2[i]
            
            temp_arr.append(sum_value)
    
        answer.append(temp_arr)
        
    return answer

print(solution([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]]))
print(solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4, 3], [2, 4, 1], [3, 1, 1]]))