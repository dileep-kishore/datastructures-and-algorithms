''' Calculating the molecular weight of a protein '''
def compute_MWt(amino_acid):
    ''' str --> int
    >>> compute_MWt('AL')
    202
    >>> compute_MWt('MNISAFKIANKLITGQGAIEQLSAELTRLNVKNPLIVTDAVLVQSGTVDLALAQLGGRCYGIFDQVKPEP')
    7445
    '''
    weights = {'A':89, 'B':133, 'C':121, 'D':133, 'E':147, 'F':165, 'G':75,
               'H':155, 'I':131, 'K':146, 'L':131, 'M':149, 'N':132, 'P':115,
               'Q':146, 'R':174, 'S':105, 'T':119, 'V':117, 'W':204, 'Y':181,
               'Z':147}
    amino_range = ''.join(weights.keys())
    mol_wt = 0
    amino_acid = amino_acid.upper().replace(' ', '').replace('\n', '')
    for dummy in amino_acid:
        if amino_range.find(dummy) == -1:
            print('Invalid input')
            raise ValueError(dummy)
        mol_wt += weights[dummy]
    mol_wt -= 18*(len(amino_acid)-1)
    return mol_wt

import doctest
doctest.testmod(verbose='true')

