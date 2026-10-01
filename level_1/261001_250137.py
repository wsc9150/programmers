# [PCCP 기출문제] 1번 / 붕대 감기

def solution(bandage, health, attacks):
    answer = 0
    time = 0
    attack_idx = 0
    heal_cnt = 0
    max_health = health
    
    while attack_idx < len(attacks):
        time += 1
        
        if time == attacks[attack_idx][0]:
            health -= attacks[attack_idx][1]
            if health <= 0:
                break
            
            attack_idx += 1
            heal_cnt = 0
        else:
            if health < max_health:
                health += bandage[1]
                heal_cnt += 1
                
                if heal_cnt == bandage[0]:
                    health += bandage[2]
                    heal_cnt = 0
                
                health = health if health <= max_health else max_health
                    
    if health <= 0:
        health = -1
        
    return health

print(solution([5, 1, 5], 30, [[2, 10], [9, 15], [10, 5], [11, 5]]))
print(solution([3, 2, 7], 20, [[1, 15], [5, 16], [8, 6]]))
print(solution([4, 2, 7], 20, [[1, 15], [5, 16], [8, 6]]))
print(solution([1, 1, 1], 5, [[1, 2], [3, 2]]))