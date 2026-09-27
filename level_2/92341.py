# 주차 요금 계산

import math

def solution(fees, records):
    answer = []
    
    car_info = {}
    
    for r in records:
        time, car_number, state = r.split()
        if car_number not in car_info:
            car_info[car_number] = [time]
        else:
            car_info[car_number].append(time)
    
    car_fee = {}
    
    for car in car_info.keys():
        time_list = car_info[car]
        if len(time_list) % 2 != 0:
            time_list.append('23:59')
        
        entire_time = 0
        for i in range(0, len(time_list), 2):
            start_hour, start_minute = time_list[i].split(':')
            end_hour, end_minute = time_list[i + 1].split(':')
            
            entire_time += (int(end_hour) * 60 + int(end_minute)) - (int(start_hour) * 60 + int(start_minute))
        
        car_fee[car] = entire_time
    
    sorted_list = sorted(car_fee.items())
    for i in sorted_list:
        fee = fees[1] if i[1] < fees[0] else fees[1] + math.ceil((i[1] - fees[0]) / fees[2]) * fees[3]
        answer.append(fee)
            
    return answer

print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
print(solution([120, 0, 60, 591], ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]))
print(solution([1, 461, 1, 10], ["00:00 1234 IN"]))