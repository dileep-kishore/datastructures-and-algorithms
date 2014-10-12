__author__ = 'dileep'
# Residue Pair preference
def pair_pref(seq):
	"""Calculating the pair preference of the protein sequences"""
	amino_acids = 'ACDEFGHIKLMNPQRSTVWY'
	pairs = [x+y for x in amino_acids for y in amino_acids if x != y]
	print(pairs)
	return len(amino_acids)

if __name__ == '__main__':
	print(pair_pref(
		'MALLPAAPGAPARATPTRWPVGCFNRPWTKWSYDEALDGIKAAGYAWTGLLTASKPLHHATATPEYLAALKQKSRHAA'))
	print(pair_pref(
		'AMENLNMDLLYMAAAVMMGLAAIGAAIGIGILGGKFLEGAARQPDLIPLLRTQFFIVMGLVDAIPMIAVGLGLYVMFAVA'))
	print(pair_pref(
		'AADVSAAVGATGQSGMTYRLGLSWDWDKSWWQTSTGRLTGYWDAGYWDAGYTYWEGGDEGAGKHSLSFAPVFVYEFAGDSIKPFIEAGIGVAASGTRVGDQNLGSSLNFEDRIGAGLKFANGQSVGVRAIHYSNAGLKQPNDGIESYSLFYKIPI'))
