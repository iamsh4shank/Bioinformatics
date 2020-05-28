def hammingDistacne(seqA, seqB):
    hamDistance = 0
    for i in range(len(seqA)):
        if seqA[i] != seqB[i]:
            hamDistance+=1
    return hamDistance
