def make_readable(seconds):
    
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    
    print(h)
    print(m)
    print(s)
    
    result = f"{h:02d}:{m:02d}:{s:02d}"
    return result
    
# best practice is similar

def make_readable(seconds):
    hours, seconds = divmod(seconds, 60 ** 2)
    minutes, seconds = divmod(seconds, 60)
    return '{:02}:{:02}:{:02}'.format(hours, minutes, seconds)
