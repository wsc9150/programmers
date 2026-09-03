# 기능개발

def solution(progresses, speeds):
    answer = []
    progresses.reverse()
    speeds.reverse()
    
    while len(progresses) > 0:
        processing = list(zip(progresses, speeds))
        progresses = [p[0] + p[1] for p in processing]
        
        deploy_cnt = 0
        while len(progresses) > 0 and progresses[-1] >= 100:
            progresses.pop()
            deploy_cnt += 1
        
        if deploy_cnt > 0:
            answer.append(deploy_cnt)
    
    return answer

print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))