# my solutions
def find_uniq(arr):
    arr.sort()
    if (arr[0] < arr[len(arr) - 1] and arr[0] < arr[len(arr) - 2]):
        n = arr[0]
    else:
        n = arr[len(arr) - 1]
    return n

#return [arr[x] for x in range(0, len(arr)) if arr.count(arr[x]) == 1][0] 
# too long exec time

# good solution :)
def find_uniq2(arr):
    arr_set = set(arr)
    for i in arr_set:
        if arr.count(i) == 1:
            return i