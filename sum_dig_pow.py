def sum_dig_pow(a, b):
    result = []
    summary = 0
    
    for i in range(a, b + 1):
        summary = sum(int(value) ** key for key, value in enumerate(str(i), 1))
        if summary == i:
            result.append(i)    
            
    return result
        

