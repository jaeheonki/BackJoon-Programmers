def solution(s, skip, index):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
                 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    word = list(s)
    rm_alpha = list(skip)
    
    for rm in rm_alpha :
        alphabet.remove(rm)
    
    for i in range(len(word)):
        c_index = alphabet.index(word[i])
        word[i] = alphabet[(c_index + index) % len(alphabet)]
        
    res = "".join(word)
        
    return res