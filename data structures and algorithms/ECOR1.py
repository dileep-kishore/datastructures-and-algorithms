# DNA digestion with ECOR1
def ecor1(dna):
    '''str --> tuple
    >>>ecor1('CTGTCAGTGGAATTCACTAGCTGA','GACAGTCACCTTAAGTGATCGACT')
    '''
    site = 'GAATTC'             #depends on the strand?
    prev_index1 = 0
    prev_index2 = -4
    next_index1 = dna[0].find(site)
    next_index2 = next_index1
    fragment = ()
    while (prev_index1 != -1) and (next_index1 != -1):
        next_index1 += 1
        fragment += ((dna[0][prev_index1:next_index1], dna[1][prev_index2+4:next_index2+4]))
        prev_index1 = next_index1
        next_index1 = dna[0][prev_index1:].find(site)
        prev_index2 = prev_index1
        next_index2 = next_index1
    fragment += ((dna[0][prev_index1:], dna[1][prev_index2+4:]))
    return fragment
