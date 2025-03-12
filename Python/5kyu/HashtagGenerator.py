def generate_hashtag(s):
    
    result = ""
    
    if s == "":
        return False
    else:
        result += "#"
        string = s.lower()
        result += string.title()
        r = result.replace(" ", "")
        if len(r) <= 140:
            return r
        else:
            return False

# best pratice

def generate_hashtag(s):
    output = "#"
    
    for word in s.split():
        output += word.capitalize()
    
    return False if (len(s) == 0 or len(output) > 140) else output
        
