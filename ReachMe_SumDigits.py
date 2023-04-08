def sumDig_nthTerm(initVal, patternL, nthTerm):
    x = initVal
    for i in range(0, nthTerm - 1):
        x += patternL[i % len(patternL)]
    x = sum(int(value) for value in dict(enumerate(str(x))).values())
    return x
