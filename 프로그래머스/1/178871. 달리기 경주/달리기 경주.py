from collections import defaultdict

def solution(players, callings):
    ranks = defaultdict(str)
    
    for i in range(len(players)) :
        ranks[players[i]] = i
    
    for call in callings :
        new_rank_win = ranks[call] - 1
        new_rank_lose = ranks[call]
        
        players[new_rank_win], players[new_rank_lose] = players[new_rank_lose], players[new_rank_win]
        
        ranks[players[new_rank_win]] = new_rank_win
        ranks[players[new_rank_lose]] = new_rank_lose
        
    
    return players