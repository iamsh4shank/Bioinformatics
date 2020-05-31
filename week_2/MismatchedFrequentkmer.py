def FrequentWords(s,k,d):
    counts = {}
    for i in range(len(s)-k+1):
        for neighbor in neighbors(s[i:i+k],d):
            if neighbor not in counts:
                counts[neighbor] = 0
            counts[neighbor] += 1
    m = max(counts.values())
    return [kmer for kmer in counts if counts[kmer] == m]

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

def hamming( seqA, seqB ):
    hamDistance = 0
    for i in range(len(seqA)):
        if seqA[i] != seqB[i]:
            hamDistance+=1
    return hamDistance

print FrequentWords('GTCGTCGTCAGCAACGTCCCATATCACGTCCCACCCAACGTAGCAACGTTATCTATCTATCCCCAGTCAGCAAGCACCCATATCTATCACGTTATCGTCACGTCCCATATCGTCACGTACGTAGCAGTCTATCTATCTATCCCCAGTCACGTGTCGTCAGCAAGCAGTCTATCTATCACGTACGTAGCAACGTTATCGTCAGCAACGTAGCAGTCAGCACCCAGTCACGTAGCAGTCAGCAACGTTATCCCCACCCATATCGTCAGCAGTCCCCACCCATATCTATCCCCAACGTGTCGTCGTCCCCACCCAAGCAGTCTATCGTCAGCATATCAGCATATCTATCACGTGTCTATCCCCAACGTGTCGTCTATCCCCACCCAAGCA',6 , 2)    
