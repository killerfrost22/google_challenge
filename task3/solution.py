def solution(xs):
    # Your code here
    if len(xs) == 0:
        return str(0)
    if len(xs) == 1:
        return str(xs[0])
        
    pos = []
    neg = []
    for x in xs:
        if x > 0: pos.append(x)
        elif x < 0: neg.append(x)
    
    pos_count = len(pos)
    neg_count = len(neg)
    
    if neg_count == 1 and pos_count ==0:
        return str(0)
    if neg_count == 0 and pos_count ==0:
        return str(0)
        
    power = 1
    for n in pos:
        power*=n
        
    if neg_count % 2 == 1:
        neg.remove(max(neg))
    for n in neg:
        power*=n
    
    return str(power)