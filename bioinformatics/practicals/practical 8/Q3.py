__author__ = 'dileep'
# Classifying proteins into Group A and B
def amino_class(seq):
	from Q1 import amino_comp
	"""Determining the type of the protein"""
	group_a = {'A': 8.47, 'D': 5.97, 'C': 1.39, 'E': 6.32, 'F': 3.91,
              'G': 7.82, 'H': 2.26, 'I': 5.71, 'K': 5.76, 'L': 8.48,
              'M': 2.21, 'N': 4.54, 'P': 4.63, 'Q': 3.82, 'R': 4.93,
              'S': 5.94, 'T': 5.79, 'V': 7.02, 'W': 1.44, 'Y': 3.58}
	group_b = {'A': 8.95, 'D': 5.91, 'C': 0.47, 'E': 4.78, 'F': 3.68,
              'G': 8.54, 'H': 1.25, 'I': 4.77, 'K': 4.93, 'L': 8.78,
              'M': 1.56, 'N': 5.74, 'P': 3.74, 'Q': 4.75, 'R': 5.24,
              'S': 8.05, 'T': 6.54, 'V': 6.76, 'W': 1.24, 'Y': 4.13}
	comp = amino_comp(seq)
	norm_a = 0.0
	norm_b = 0.0
	for amino in comp:
		norm_a += (comp[amino] - group_a[amino]) ** 2
		norm_b += (comp[amino] - group_b[amino]) ** 2
	if norm_a < norm_b:
		return 'The protein belongs to group A'
	else:
		return 'The protein belongs to group B'

if __name__ == '__main__':
	print(amino_class('MALLPAAPGAPARATPTRWPVGCFNRPWTKWSYDEALDGIKAAGYAWTGLLTASKPLHHATATPEYLAALKQKSRHAA'))