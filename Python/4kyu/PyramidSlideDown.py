# actually working from the bottom to find the best way. Not sure I fully understand the solves yet

def longest_slide_down(pyramid):
    if len(pyramid) == 1:
        return pyramid[0][0]
    
    last_layer = pyramid[-1]
    add_layer = []
    for i in range(1, len(last_layer)):
        add_layer.append(max(last_layer[i], last_layer[i-1]))
     # zip returns a zip object by matching two tuples, the one with the east decides the length of the new iterator   
    pyramid[-2] = [a + b for a, b in zip(pyramid[-2], add_layer)]
    
    return longest_slide_down(pyramid[:-1])

# best practice

ef longest_slide_down(p):
    # pop removes the element at the specified position
    res = p.pop()
    while p:
        tmp = p.pop()
        res = [tmp[i] + max(res[i],res[i+1])  for i in range(len(tmp))] 
    return res.pop()
