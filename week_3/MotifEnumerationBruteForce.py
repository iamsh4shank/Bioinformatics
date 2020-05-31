def ApproximatePatternCount(Text, Pattern, d):
    count=0
    for i in range(len(Text)-len(Pattern)+1):
        candidate=Text[i:i+len(Pattern)]
        if HammingDistance(Pattern,candidate)<=d:
            count=count+1
    return count

def HammingDistance(p, q):
    count=0
    for i in range(len(p)):
        if p[i]!=q[i]:
            count=count+1
    return count

def Neighbors(Pattern, d):
    if d == 0:
        return Pattern
    if len(Pattern) == 1:
        return ["A", "C", "G", "T"]
    Neighborhood = []
    for item in Neighbors(Pattern[1:], d):
        if len([x for x, y in zip(item, Pattern[1:]) if x != y]) < d:
            for i in ["A", "C", "G", "T"]:
                Neighborhood += [i + item]
        else:
            Neighborhood += [Pattern[:1] + item]
    return Neighborhood

def MotifEnumeration(Dna, k, d):
    Patterns = []
    if d == 0: # No differences admitted
        for i in range(len(Dna[0])-k+1):
            pattern = Dna[0][i:(i+k)]
            other_strings = []
            for string in Dna:
                other_strings.append(ApproximatePatternCount(string, pattern, d))
            if 0 not in other_strings and pattern not in Patterns:
                Patterns.append(pattern)
    else:
        for i in range(len(Dna[0])-k+1): # Define the potential patterns' from the first string in Dna
            pattern = Dna[0][i:(i+k)]
            Neigh = (Neighbors(pattern, d)) # patterns' differing from pattern in d
            for kmer in Neigh:
                other_strings = []
                for string in Dna:
                    other_strings.append(ApproximatePatternCount(string, kmer, d)) # Times pattern' appears with d differences in the other strings
                if 0 not in other_strings and kmer not in Patterns: # Append if present in all strings
                    Patterns.append(kmer)
    return Patterns
