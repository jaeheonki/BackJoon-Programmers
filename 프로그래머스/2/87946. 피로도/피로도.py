from itertools import permutations

def solution(k, dungeons):
    #1 ~ 던전의 개수까지 모든 값을 가지는 순열 모두 반환
    orders = list(permutations(range(len(dungeons))))
    
    
    max_dungeon_cnt = 0
    #모든 던전 가는 경우의 수 순회
    for order in orders :
        my_tired = k
        current_dungeon_cnt = 0
        
        #던전 돌기
        for dungeon_idx in order :
            if my_tired >= dungeons[dungeon_idx][0] :
                current_dungeon_cnt += 1
                my_tired -= dungeons[dungeon_idx][1]
            else:
                break
        #다 돌았으면 max_dungeon count 갱신
        max_dungeon_cnt = max(max_dungeon_cnt, current_dungeon_cnt)
    
    return max_dungeon_cnt
                