def likes(names):
    
    if len(names) == 0:
        return "no one likes this"
    elif len(names) == 1:
        return str(names[0]) + " likes this"
    elif len(names) == 2:
        return str(names[0]) + " and " + str(names[1]) + " like this"
    elif len(names) == 3:
        return str(names[0]) + ", " + str(names[1]) + " and " + str(names[2]) + " like this"
    elif len(names) >= 4:
        print(str(names[0]) + ", " + str(names[1]) + " and " + str(len(names) - 2) + " others like this")
        return str(names[0]) + ", " + str(names[1]) + " and " + str(len(names) - 2) + " others like this"

  # better practice

def likes(names):
    n = len(names)
    return {
        0: 'no one likes this',
        1: '{} likes this', 
        2: '{} and {} like this', 
        3: '{}, {} and {} like this', 
        4: '{}, {} and {others} others like this'
    }[min(4, n)].format(*names[:3], others=n-2)
