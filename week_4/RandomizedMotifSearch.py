from random import randint
def HammingDistance(seqA, seqB):
    hamDistance = 0
    for i in range(len(seqA)):
        if seqA[i] != seqB[i]:
            hamDistance+=1
    return hamDistance

def score(motifs):
	'''Returns the score of the dna list motifs.'''
	score = 0
	for i in range(len(motifs[0])):
		motif = ''.join([motifs[j][i] for j in range(len(motifs))])
		score += min([HammingDistance(motif, homogeneous*len(motif)) for homogeneous in 'ACGT'])
	return score

def profile(motifs):
	'''Returns the profile of the dna list motifs.'''
	prof = []
	for i in range(len(motifs[0])):
		col = ''.join([motifs[j][i] for j in range(len(motifs))])
		prof.append([float(col.count(nuc))/float(len(col)) for nuc in 'ACGT'])
	return prof

def profile_most_probable_kmer(dna, k, prof):
	'''Return the profile most probable k-mer in a given dna sequence.'''
	# A dictionary relating nucleotides to their position within the profile.
	nuc_loc = {nucleotide:index for index,nucleotide in enumerate('ACGT')}
	# Initialize the maximum probabily.
	max_prob = [-1, None]
	# Compute the probability of the each k-mer, store it if it's currently a maximum.
	for i in range(len(dna)-k+1):
		current_prob = 1
		for j, nucleotide in enumerate(dna[i:i+k]):
			current_prob *= prof[j][nuc_loc[nucleotide]]
		if current_prob > max_prob[0]:
			max_prob = [current_prob, dna[i:i+k]]

	return max_prob[1]
def profile_with_pseudocounts(motifs):
	'''Returns the profile of the dna list motifs.'''
	prof = []
	for i in range(len(motifs[0])):
		col = ''.join([motifs[j][i] for j in range(len(motifs))])
		prof.append([float(col.count(nuc)+1)/float(len(col)+4) for nuc in 'ACGT'])
	return prof


def motifs_from_profile(profile, dna, k):
	return [profile_most_probable_kmer(seq,k,profile) for seq in dna]

def randomized_motif_search(dna,k,t):
	# Randomly generate k-mers from each sequence in the dna list.
	rand_ints = [randint(0,len(dna[0])-k) for a in range(t)]
	motifs = [dna[i][r:r+k] for i,r in enumerate(rand_ints)]

	# Initialize the best score as a score higher than the highest possible score.
	best_score = [score(motifs), motifs]

	# Iterate motifs.
	while True:
		current_profile = profile_with_pseudocounts(motifs)
		motifs = motifs_from_profile(current_profile, dna, k)
		current_score = score(motifs)
		if current_score < best_score[0]:
			best_score = [current_score, motifs]
		else:
			return best_score

if __name__ == "__main__":
	
    k,t = [int(a) for a in input().strip().split(" ")]
    Dna = []
    for _ in range(t):
        Dna.append(input())
	#use this if you are taking input from file
	'''with open('input.txt') as input_data:
		k,t = map(int, input_data.readline().split())
		dna_list = [line.strip() for line in input_data.readlines()]'''
    best_motifs = [k*t, None]
    # Repeat the radomized motif search 1000 times.
    for repeat in range(1000):
        current_motifs = randomized_motif_search(Dna,k,t)
        if current_motifs[0] < best_motifs[0]:
            best_motifs = current_motifs
    gfh = best_motifs[1]
    for i in gfh:
        print (i),


