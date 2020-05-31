def HammingDistance(seqA, seqB):
    hamDistance = 0
    for i in range(len(seqA)):
        if seqA[i] != seqB[i]:
            hamDistance+=1
    return hamDistance

def distanceBetweenPatternAndStrings(Pattern, Dna): #distanceBetweenPatternAndStrings(Pattern, Dna)
    k = len(Pattern) 
    Distance = 0 
    for string in  Dna: 
        hammingDistance = float("inf") #
        for i in range(0, len(string)-k+1): 
            if hammingDistance > HammingDistance(Pattern, string[i:i+k]): #
                hammingDistance = HammingDistance(Pattern, string[i:i+k]) #
        Distance = Distance + hammingDistance
    return Distance

        
