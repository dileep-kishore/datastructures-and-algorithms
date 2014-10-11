# Re-engineered translation machinery
def translateDNAX(inputFile):
    ''' DNA sequence --> Protein sequence '''
    # Opening the input file
    dna_file = open(inputFile, 'r+')
    bases = ['T', 'C', 'A', 'G']
    # Constructing the codon table
    codons = [a+b+c for a in bases for b in bases for c in bases]
    amino_acids = 'FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
    dna = dna_file.read()
    n_dna = dna.count('>')
    if n_dna == 0:
        n_dna = 1
        dna_seq = dna.upper().replace('\n', '').replace(' ', '').replace('\r', '')
    else:
        dna_seq = dna.split('>')
        dna_seq = dna_seq[1:]
        for dummy1 in range(n_dna):
            index = dna_seq[dummy1].find('\n')
            dna_seq[dummy1] = dna_seq[dummy1][index+1:]
            dna_seq[dummy1] = dna_seq[dummy1].upper().replace('\n', '').replace(' ', '').replace('\r', '')
    codon_dict = dict(zip(codons, amino_acids))
    quad_dict = {'TAGA': 'q', 'TGAG': 's', 'TGAC': 's'}
    start_dict = {'TTG': 'M', 'CTG': 'M', 'ATG': 'M'}
    comp_dict = {'T': 'A', 'A': 'T', 'G': 'C', 'C': 'G'}
    protein = ''
    dna_trans = dna_seq
    protein = ['']
    frame = [0, 1, 2, 0, 1, 2]
    start_list = list(start_dict.keys())
    quad_list = list(quad_dict.keys())
    # Translation
    for iter2 in range(n_dna):
        pro_length = []
        orf_protein = ['']
        for counter, orf in zip(range(6), frame):
            flag = True
            n_base = orf
            while n_base < len(dna_trans[iter2]):
                if (dna_trans[iter2][n_base:n_base+3] in start_list) and flag:
                    orf_protein[counter] += start_dict[dna_trans[iter2][n_base:n_base+3]]
                    flag = False
                else:
                    if (dna_trans[iter2][n_base:n_base+4] in quad_list) and flag == False:
                        orf_protein[counter] += quad_dict[dna_trans[iter2][n_base:n_base+4]]
                        n_base += 1
                    else:
                        if len(dna_trans[iter2][n_base:n_base+3]) < 3:
                            break
                        if codon_dict[dna_trans[iter2][n_base:n_base+3]] == '*':
                            flag = True
                            orf_protein[counter] += '*'
                        if flag == False:
                            orf_protein[counter] += codon_dict[dna_trans[iter2][n_base:n_base+3]]
                n_base += 3
            temp_proteins = orf_protein[counter].split('*')
            temp_proteins = [pep for pep in temp_proteins if pep != '']
            if temp_proteins != []:
                orf_protein[counter] = max(temp_proteins, key=len)
            else:
                orf_protein[counter] = ''
            orf_protein.append('')
            pro_length.append(len(orf_protein[counter]))
            if orf == 2:
                dna_trans[iter2] = dna_trans[iter2][::-1]
                temp = ''
                for rev in range(0, len(dna_trans[iter2])):
                    temp += comp_dict[dna_trans[iter2][rev]]
                dna_trans[iter2] = temp
        longest_orf = pro_length.index(max(pro_length))
        protein[iter2] += orf_protein[longest_orf]
        protein.append('')
    protein = protein[:n_dna]
    # Writing protein sequence into the file
    protein_file = ''
    for count, prot in zip(range(n_dna), protein):
        protein_file += '>Sequence'+ str(count+1) + '\n' + prot + '\n'
    result = open('xxxxx-protein.faa', 'w+')
    result.write(protein_file)
    dna_file.close()
    result.close()
    return protein
