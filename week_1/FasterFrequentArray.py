nucs = {'A':0,'C':1,'G':2,'T':3}
def PatternToNumber(Pattern):
    index = 0
    power = []
    for i in range(len(Pattern)-1,-1,-1):
        power.append(i)
    for i in range(len(Pattern)):
        index += nucs[Pattern[i]]*(4**power[i])
    return index

def numberToPattern(index, k):
    count = 0
    pattern = []
    val = index
    while count != k:
        if val == 0:
            pattern.append(0)
        else:
            pattern.append(val%4)
            val = int(val/4)
        count = count + 1
    pattern.reverse()
    for i in range(k):
        i_nucleotide = pattern[i]
        if i_nucleotide == 0:
            pattern[i] = 'A'
        elif i_nucleotide == 1:
            pattern[i] = 'C'
        elif i_nucleotide == 2:
            pattern[i] = 'G'
        else :
            pattern[i] = 'T'
    return pattern

def ComputingFrequencies(Text, k):
    frequencyArray = []
    for i in range(4**k):
        frequencyArray.append(0)
    for i in range(len(Text)-k+1):
        pattern = Text[i:i+k]
        j = PatternToNumber(pattern)
        frequencyArray[j] = frequencyArray[j]+1
    return frequencyArray

def FasterFrequentArray(Text, k):
    frequentPatterns = set()
    frequency = ComputingFrequencies(Text, k)
    maxCount = max(frequency)
    for i in range(4**k):
        if frequency[i] == maxCount:
            pattern = numberToPattern(i,k)
            frequentPatterns.add(pattern)
    return frequentPatterns

#Main
Text = 'AAGTTTCTGTAAGCTGTAAGCTCTTAACTGTAAGCTCTTAACTGAGTCCTGGAATACAAGTTTCTGAGTCCTGGAATACCTTAACTCTTAACTCTTAACTCTTAACTGAGTCCTCTTAACTGAGTCCTAAGTTTCTAAGTTTCTGGAATACGAGTCCTGTAAGCTGTAAGCTGTAAGCTCTTAACTGGAATACAAGTTTCTGTAAGCTCTTAACTGAGTCCTGTAAGCTAAGTTTCTGGAATACGTAAGCTCTTAACTGGAATACAAGTTTCTCTTAACTGTAAGCTGAGTCCTGTAAGCTCTTAACTAAGTTTCTCTTAACTGGAATACGTAAGCTGAGTCCTGGAATACAAGTTTCTAAGTTTCTGTAAGCTGGAATACAAGTTTCTCTTAACTAAGTTTCTCTTAACTGAGTCCTCTTAACTGTAAGCTGGAATACCTTAACTGGAATACGTAAGCTGTAAGCTGGAATACCTTAACTGAGTCCTGAGTCCTGAGTCCTGGAATACGTAAGCTCTTAACTAAGTTTCTGGAATACGTAAGCTGTAAGCTGTAAGCTAAGTTTCTGGAATACGGAATACGTAAGCTGGAATACGAGTCCTAAGTTTCTGGAATACGGAATACGAGTCCTAAGTTTCTCTTAACTGGAATACGTAAGCTCTTAACTAAGTTTCTGAGTCCTAAGTTTCTGTAAGCTGTAAGCTGTAAGCTAAGTTTCTGAGTCCTCTTAACTGAGTCCTGTAAGCTAAGTTTCTAAGTTTCTCTTAACTGGAATACGTAAGCTAAGTTTCTGTAAGCT'
K = 14
A = FasterFrequentArray(Text,K)
print(A)