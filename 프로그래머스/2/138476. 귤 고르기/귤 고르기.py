from collections import defaultdict
def solution(k, tangerine):
    sizes = defaultdict(int)
    box = 0
    res = 0
    for t in tangerine :
        sizes[t] += 1
    
    sizes = dict(sorted(sizes.items(), key = lambda x: x[1], reverse = True))
    
    for size, value in sizes.items() :
        box += value
        res += 1
        if box >= k:
            return res
    
    return res