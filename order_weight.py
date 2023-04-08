def order_weight(strng):
    start_list = sorted(strng.split(' '))
    finish_list = sorted(start_list, key=weights)

    return " ".join(finish_list)



def weights(n):
    return sum([int(elem) for elem in n])


print(order_weight("2000 10003 1234000 44444444 9999 11 11 22 123"))