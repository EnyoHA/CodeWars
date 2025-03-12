#Wrong track to start but learnt a lot from it

def order_weight(strng):
"""
    if strng == "":
        return ""
    
    s = strng.strip().split()
    
    print(s)
    
    def weight(num):
        return
     # print(strng)
    result = ""
    r = []
    if strng == "":
        return ""
    else:
        s = strng.split(" ")
        #print(s)
        for num in s:
            nums = list(map(int, num))
            #print(nums)
            n = sum(nums)
            #print(n)
            
            r.append(n)
        z = zip(r,s)
        print(r)
        k = sorted(z, key=lambda x: x[0])
        print(k)
        second_values = list(map(lambda x: x[1], k))
        print(second_values)
        return " ".join(second_values)
        # return " ".join(list(map(lambdax: x[1], k)))
        
      # couldn't get this as the order was wrong
  """
def order_weight(strng):
    
    if strng == "":
        return ""
    
    s = strng.strip().split()
    
    # define sorting criteria
    
    """
    def weight(num):
        return (sum(int(digit) for digit in num), num)
    
    """
    def weight(num):
    # Step 1: Convert each character (digit) in the string 'num' to an integer
        digits = []
        for digit in num:
            digits.append(int(digit))

        # Step 2: Sum the list of integers
        digit_sum = sum(digits)

        # Step 3: Return a tuple of (digit_sum, num)
        return (digit_sum, num)
    
    sorted_list = sorted(s, key=weight)
    
    
    return " ".join(sorted_list)


# best practice

def order_weight(_str):
    return ' '.join(sorted(sorted(_str.split(' ')), key=lambda x: sum(int(c) for c in x)))
