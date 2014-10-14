__author__ = 'dileep'
# Hydrophobicity profile for different windows lengths
from pylab import *
def hydro_win(win_len, seq):
    """Determining hydrophobicity profile of seq for windows of 9 and 19"""
    hydro_dict = {'A': 13.85, 'D': 11.61, 'C': 15.37, 'E': 11.38, 'F': 13.93,
                  'G': 13.34, 'H': 13.82, 'I': 15.28, 'K': 11.58, 'L': 14.13,
                  'M': 13.86, 'N': 13.02, 'P': 12.35, 'Q': 12.61, 'R': 13.10,
                  'S': 13.39, 'T': 12.70, 'V': 14.56, 'W': 15.48, 'Y': 13.88}
    hydrophobicity = [0.0] * len(seq)
    for i, res in enumerate(seq):
        if i < win_len // 2:
            right = ''
            left = seq[0:win_len]
        elif i > len(seq) - win_len // 2 - 1:
            right = seq[len(seq)-win_len:len(seq)]
            left = ''
        else:
            left = seq[i - win_len // 2 : i]
            right = seq[i : i + win_len // 2 + 1]
        for dummy in left + right:
            hydrophobicity[i] += hydro_dict[dummy] / win_len
    x_values = range(len(seq))
    plot(x_values, hydrophobicity)
    show()
    return hydrophobicity

if __name__ == '__main__':
    print(hydro_win(19,
    'MALLPAAPGAPARATPTRWPVGCFNRPWTKWSYDEALDGIKAAGYAWTGLLTASKPSLHHATATPEYLAALKQKSRHAA'))
    print(hydro_win(19, 'AMENLNMDLLYMAAAVMMGLAAIGAAIGIGILGGKFLEGAARQPDLIPLLRTQFFIVMGLVDAIPMIAVGLGLYVMFAVA'))
    print(hydro_win(19, 'AADVSAAVGATGQSGMTYRLGLSWDWDKSWWQTSTGRLTGYWDAGYTYWEGGDEGAGKHSLSFAPVFVYEFAGDSIKPFIEAGIGVAAFSGTRVGDQNLGSSLNFEDRIGAGLKFANGQSVGVRAIHYSNAGLKQPNDGIESYSLFYKIP'))
