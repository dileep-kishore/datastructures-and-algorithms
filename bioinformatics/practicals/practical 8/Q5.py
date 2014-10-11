__author__ = 'dileep'
# Hydrophobicity profile
def hydrophobicity(seq):
	"""Determining the hydrophobicity profile"""
	hydro_dict = {'A': 13.85, 'D': 11.61, 'C': 15.37, 'E': 11.38, 'F': 13.93,
                  'G': 13.34, 'H': 13.82, 'I': 15.28, 'K': 11.58, 'L': 14.13,
                  'M': 13.86, 'N': 13.02, 'P': 12.35, 'Q': 12.61, 'R': 13.10,
                  'S': 13.39, 'T': 12.70, 'V': 14.56, 'W': 15.48, 'Y': 13.88}
	hyd_pro = []
	for res in seq:
		hyd_pro += [hydro_dict[res]]
	return hyd_pro

if __name__ == '__main__':
	print(hydrophobicity('MALLPAAPGAPARATPTRWPVGCFNRPWTKWSYDEALDGIKAAGYAWTGLLTASKPLHHATATPEYLAALKQKSRHAA'))