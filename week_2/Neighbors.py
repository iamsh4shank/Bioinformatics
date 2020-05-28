def hamming( seqA, seqB ):
    hamDistance = 0
    for i in range(len(seqA)):
        if seqA[i] != seqB[i]:
            hamDistance+=1
    return hamDistance

def neighbors( s, d ):
    if d == 0:
        return [s]
    if len(s) == 1:
        return ['A','C','G','T']
    out = []
    for neighbor in neighbors(s[1:],d):
        if hamming(s[1:],neighbor) < d:
            out.extend(['A'+neighbor,'C'+neighbor,'G'+neighbor,'T'+neighbor])
        else:
            out.append(s[0] + neighbor)
    return out

x = neighbors('GGTACTAAAT', 3)
for i in x:
    print i,