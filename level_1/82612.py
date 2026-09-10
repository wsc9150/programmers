# 부족한 금액 계산하기

def solution(price, money, count):
    answer = -1
    price_sum = sum([i * price for i in range(1, count + 1)])
    answer = price_sum - money if price_sum > money else 0
    return answer

print(solution(3, 20, 4))