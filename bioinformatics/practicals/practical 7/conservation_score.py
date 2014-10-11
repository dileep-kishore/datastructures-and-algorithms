__author__ = 'dileep'
# Conservation score using unweighted frequency and entropy based measure

def conservation(seq) -> list:
	"""Gives conservation scores
	:rtype : list
	:type seq: str
	:param seq: input file
	"""
	import numpy
	import math

	seq_file = open(seq, "r+")
	sequences = seq_file.read().upper()
	sequences = sequences.split('\n')
	sequences = [sequences[i].split(' ') for i in range(len(sequences))]
	sequences = [sequences[i][j] for i in range(len(sequences)) for j in
	             range(len(sequences[i])) if sequences[i][j] != '']
	sequences = [sequences[i] for i in range(len(sequences)) if sequences[i][
		0] != '*' and sequences[i][0] != '.' and sequences[i][0] != ':']
	sequences = [sequences[i] for i in range(len(sequences)) if i % 2 == 1]
	sequences = [sequences[i] + sequences[i + 12] + sequences[i + 24] for i
	             in range(12)]
	amino_acids = list(set('FLSYCWLPHQRIMTNKSRVADEG'))
	freq = numpy.matrix([[0.0] * len(amino_acids)] * len(sequences[1]))
	for x in range(len(sequences[1])):
		for y in range(len(sequences)):
			if sequences[y][x] in amino_acids:
				ind = amino_acids.index(sequences[y][x])
				freq[x, ind] += 1 / 12
	entropy = []
	for x in range(len(sequences[1])):
		temp = 0.0
		for y in range(len(amino_acids)):
			if freq[x, y] != 0.0:
				temp += freq[x, y] * math.log(freq[x, y])
		entropy += [temp]
	return entropy


print(conservation('clustal_set1'))
