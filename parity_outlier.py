def find_outlier(integers):
    even_nums = []
    for num in integers:
        if (num % 2 == 0) and (num != 0):
            even_nums.append(num)
    if (len(even_nums) != 1):
        for each in integers:
            if (each % 2 != 0):
                return each
    elif (len(even_nums) == 1):
        return even_nums[0]


def find_outlier2(integers):
    odds = [x for x in int if x % 2 != 0]
    evens= [x for x in int if x%2==0]
    return odds[0] if len(odds)<len(evens) else evens[0]

print(find_outlier([2, 4, 6, 8, 10, 3]))
