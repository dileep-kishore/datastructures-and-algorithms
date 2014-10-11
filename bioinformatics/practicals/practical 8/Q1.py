__author__ = 'dileep'
# Amino Acid composition
def amino_comp(seq):
	"""Calculating amino acid composition
	:rtype : list
	"""
	seq_len = len(seq)
	amino_acids = list(set('FLSYCWLPHQRIMTNKSRVADEG'))
	amino_acids.sort()
	ind = list(range(20))
	amino_dict = dict(zip(amino_acids, ind))
	seq = seq.upper()
	amino_count = [0.0] * 20
	for res in seq:
		amino_count[amino_dict[res]] += 1
	amino_count = [i / seq_len * 100 for i in amino_count]
	comp_dict = dict(zip(amino_acids, amino_count))
	return comp_dict

if __name__ == '__main__':
	print(amino_comp(
		'MALLPAAPGAPARATPTRWPVGCFNRPWTKWSYDEALDGIKAAGYAWTGLLTASKPLHHATATPEYLAALKQKSRHAA'))
	print(amino_comp(
		'AMENLNMDLLYMAAAVMMGLAAIGAAIGIGILGGKFLEGAARQPDLIPLLRTQFFIVMGLVDAIPMIAVGLGLYVMFAVA'))
	print(amino_comp(
		'AADVSAAVGATGQSGMTYRLGLSWDWDKSWWQTSTGRLTGYWDAGYWDAGYTYWEGGDEGAGKHSLSFAPVFVYEFAGDSIKPFIEAGIGVAASGTRVGDQNLGSSLNFEDRIGAGLKFANGQSVGVRAIHYSNAGLKQPNDGIESYSLFYKIPI'))
