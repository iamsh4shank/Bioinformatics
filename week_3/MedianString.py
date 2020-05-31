def hamming(p1, p2):
    d = 0
    for i in range(len(p1)):
        if p1[i] != p2[i]:
            d += 1
    return(d)

def MedianString(Dna,k):
	Dis = float('inf')
	l = k
	answ = ''
	possible_kmer = []
	from itertools import permutations
	for item in permutations('ATGCATGC', k):
		possible_kmer.append(''.join(item))
		possible_kmer = list(set(possible_kmer))
	for Pattern in possible_kmer:
		dis = 0
		for dna in Dna:
			HamDis = float('inf')
			for i in range(len(dna) - l):
				k_mer = dna[i:i+l]
				if HamDis > hamming(Pattern, k_mer):
					HamDis = hamming(Pattern, k_mer)
			dis +=HamDis
		if Dis > dis:
			Dis = dis
			answ = Pattern
	return(answ)

