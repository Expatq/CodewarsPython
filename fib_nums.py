def productfib(prod):
    cur_value = 0
    x = 0
    fib1 = 0
    fib2 = 1

    # creating a loop that finds nearest with prod value
    while cur_value < prod:
        x += 1
        fib1 = fib_list(x)
        fib2 = fib_list(x+1)
        cur_value = fib1 * fib2

    if (cur_value == prod):
        return [fib1, fib2, True]
    return [fib1, fib2, False]

# creating fib nums list (return value with n index)
def fib_list(n):
    a, b = 1, 1
    for i in range(n - 1):
        a, b = b, a+b
    return a

#another solution
'''
def productFib(prod):
  a, b = 0, 1
  while prod > a * b:
    a, b = b, a + b
  return [a, b, prod == a * b]
'''