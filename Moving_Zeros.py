def move_zeros(array):
    answ_arr = [elem for elem in array if elem != 0]
    i = len(array) - len(answ_arr)
    
    for n in range(i):
        answ_arr.append(0)

    return answ_arr