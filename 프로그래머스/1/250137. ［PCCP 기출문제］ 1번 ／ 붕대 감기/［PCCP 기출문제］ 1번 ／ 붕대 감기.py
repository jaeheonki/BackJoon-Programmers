def solution(bandage, health, attacks):
    max_health = health
    time_now = 0
    for attack in attacks :
        healing_time = attack[0] - time_now
        
        #healing time
        if healing_time // bandage[0] >= 1 :
            health += (healing_time // bandage[0]) * bandage[2]
            
        health += healing_time * bandage[1]
        
        if health > max_health :
            health = max_health
            
        #attack
        health -= attack[1]
        if health <= 0 :
            return -1
        time_now = attack[0] + 1
        
    return health