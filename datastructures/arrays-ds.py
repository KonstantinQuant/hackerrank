def reverseArray(a):
    result = [0] * int(len(a))
    
    for index in range(len(a)):
        result[index] = a[-index-1]
        
    return result
