def Skew(Pattern):
    skewArray = []
    for i in range(len(Pattern)+1):
        skewArray.append(0)
    for i in range(len(Pattern)):
        if Pattern[i] == 'C':
            skewArray[i+1] = skewArray[i]-1
        elif  Pattern[i] == 'G':
            skewArray[i+1] = skewArray[i]+1
        else:
            skewArray[i+1] = skewArray[i]
    return skewArray
