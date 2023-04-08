a1 = ["arp", "live", "strong"]
a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

def in_array (arr1, arr2):
    result = []
    for a2 in arr2:
        for a1 in arr1:
            if a1 in a2 and a1 not in result:
                result.append(a1)
    return sorted(result)

print(in_array(a1, a2))
