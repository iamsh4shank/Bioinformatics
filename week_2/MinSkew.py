def MinSkew(Pattern):
    skewArray = []
    maxSkewArray = []
    min = 0
    for i in range(len(Pattern)+1):
        skewArray.append(0)
    for i in range(len(Pattern)):
        if Pattern[i] == 'C':
            skewArray[i+1] = skewArray[i]-1
        elif  Pattern[i] == 'G':
            skewArray[i+1] = skewArray[i]+1
        else:
            skewArray[i+1] = skewArray[i]
    for i in range(len(skewArray)):
        if min>skewArray[i]:
            min = skewArray[i]
    for i in range(len(skewArray)):
        if skewArray[i] == min:
            maxSkewArray.append(i)
    return maxSkewArray