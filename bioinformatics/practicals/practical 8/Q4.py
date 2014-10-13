__author__ = 'dileep'
# Residue Pair preference
def pair_pref(seq):
	"""Calculating the pair preference of the protein sequences"""
	amino_acids = 'ACDEFGHIKLMNPQRSTVWY'
	pairs = [x+y for x in amino_acids for y in amino_acids]
	paired_count = [0] * 400
	for i, dummy in enumerate(pairs):
		pref_count = seq.count(dummy)
		if dummy[0] == dummy[1]:
			pref_count_a = seq.count(dummy[0])
			pref_count_b = 0
			pref_count += seq.count(dummy[0] * 3)
		else:
			pref_count_a = seq.count(dummy[0])
			pref_count_b = seq.count(dummy[1])
		if pref_count_a + pref_count_b == 0:
			pref_count = 0
			pref_count_a = 1
		paired_count[i] = pref_count * 100 / (pref_count_a + pref_count_b)
	paired_dict = dict(zip(pairs, paired_count))
	return paired_dict

if __name__ == '__main__':
	print(pair_pref(
		'MALLPAAPGAPARATPTRWPVGCFNRPWTKWSYDEALDGIKAAGYAWTGLLTASKPSLHHATATPEYLAALKQKSRHAA'))
	print(pair_pref('AMENLNMDLLYMAAAVMMGLAAIGAAIGIGILGGKFLEGAARQPDLIPLLRTQFFIVMGLVDAIPMIAVGLGLYVMFAVA'))
	print(pair_pref('AADVSAAVGATGQSGMTYRLGLSWDWDKSWWQTSTGRLTGYWDAGYTYWEGGDEGAGKHSLSFAPVFVYEFAGDSIKPFIEAGIGVAAFSGTRVGDQNLGSSLNFEDRIGAGLKFANGQSVGVRAIHYSNAGLKQPNDGIESYSLFYKIP'))
