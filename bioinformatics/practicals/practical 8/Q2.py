__author__ = 'dileep'
# Calculating the molecular weight of a protein
def prot_wt(amino_acid):
	"""Computing the molecular weight of the protein"""
	weights = {'A': 85, 'C': 115, 'D': 130, 'E': 145, 'F': 160, 'G': 70,
	           'H': 150, 'I': 125, 'K': 145, 'L': 125, 'M': 143, 'N': 130,
	           'P': 110, 'Q': 140, 'R': 170, 'S': 100, 'T': 115, 'V': 110,
	           'W': 200, 'Y': 181}
	amino_range = ''.join(weights.keys())
	mol_wt = 0
	amino_acid = amino_acid.upper().replace(' ', '').replace('\n', '')
	for dummy in amino_acid:
		if amino_range.find(dummy) == -1:
			print('Invalid input')
			raise ValueError(dummy)
		mol_wt += weights[dummy]
	mol_wt -= 18 * (len(amino_acid) - 1)
	return mol_wt

if __name__ == '__main__':
	print(prot_wt('MALLPAAPGAPARATPTRWPVGCFNRPWTKWSYDEALDGIKAAGYAWTGLLTASKPLHHATATPEYLAALKQKSRHAA'))