# 스킬트리

def solution(skill, skill_trees):
    answer = 0
    
    for skill_tree in skill_trees:
        skill_tree = list(skill_tree)
        skill_tree.reverse()
        
        skill_idx = 0
        
        while skill_tree:
            if skill_tree[-1] not in skill:
                skill_tree.pop()
            else:
                if skill_tree[-1] == skill[skill_idx]:
                    skill_tree.pop()
                    skill_idx += 1
                else:
                    break
        
        if len(skill_tree) == 0:
            answer += 1
    
    return answer

print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))