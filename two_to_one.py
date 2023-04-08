def longest(a1, a2):
    return "".join(sorted([c for c in set(a1 + a2)]))

print(longest("aretheyhere", "yestheyarehere"))
