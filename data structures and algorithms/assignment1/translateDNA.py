# Translate a DNA sequence to a protein sequence
def translateDNA(inputFile, translationTable, splice = True):
    ''' DNA sequence --> Protein sequence '''
    # Opening the input files
    dna_file = open(inputFile, 'r+')
    codon_file = open(translationTable, 'r+')
    dna = dna_file.read()
    # Getting the sequences as a list of strings
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
    # Contructing codon dictionaries
    codon_table = codon_file.read().replace(' ', '').split('\n')
    amino_acids = codon_table[0].split('=')[1]
    starts = codon_table[1].split('=')[1]
    base1 = codon_table[2].split('=')[1]
    base2 = codon_table[3].split('=')[1]
    base3 = codon_table[4].split('=')[1]
    codons = [base1[i]+base2[i]+base3[i] for i in range(len(base1))]
    codon_dict = dict(zip(codons, amino_acids))
    start_dict = dict(zip(codons, starts))
    start_dict = {code:start for code, start in start_dict.items() if start != '-'}
    comp_dict = {'T': 'A', 'A': 'T', 'G': 'C', 'C': 'G'}
    dna_spliced = ['']
    # Splicing the sequence
    if splice:
        for iter1 in range(n_dna):
            dna_spliced[iter1] = dna_seq[iter1].replace('GTA', 'x').replace('CAG', 'y')
            ind1 = dna_spliced[iter1].find('x')
            ind2 = dna_spliced[iter1].find('y', ind1)
            while (ind1 != -1) and (ind2 != -1):
                splice_prod = dna_spliced[iter1].split(dna_spliced[iter1][ind1:ind2+1])
                dna_spliced[iter1] = ''.join(splice_prod)
                ind1 = dna_spliced[iter1].find('x', ind1)
                ind2 = dna_spliced[iter1].find('y', ind1)
            dna_spliced[iter1] = dna_spliced[iter1].replace('y', 'CAG').replace('x', 'GTA')
            dna_spliced.append('')
        dna_trans = dna_spliced[:n_dna]
    else:
        dna_trans = dna_seq
    protein = ['']
    frame = [0, 1, 2, 0, 1, 2]
    start_list = list(start_dict.keys())
    # Translation
    for iter2 in range(n_dna):
        pro_length = []
        orf_protein = ['']
        for counter, orf in zip(range(6), frame):
            flag = True
            for n_base in range(orf, len(dna_trans[iter2]), 3):
                if (dna_trans[iter2][n_base:n_base+3] in start_list) and flag:
                    orf_protein[counter] += start_dict[dna_trans[iter2][n_base:n_base+3]]
                    flag = False
                else:
                    if len(dna_trans[iter2][n_base:n_base+3]) < 3:
                        break
                    if codon_dict[dna_trans[iter2][n_base:n_base+3]] == '*':
                        flag = True
                        orf_protein[counter] += '*'
                    if flag == False:
                        orf_protein[counter] += codon_dict[dna_trans[iter2][n_base:n_base+3]]
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
    # Writing the protein sequence into the file
    protein_file = ''
    for count, prot in zip(range(n_dna), protein):
        protein_file += '>Sequence'+ str(count+1) + '\n' + prot + '\n'
    result = open('xxxxx-protein.faa', 'w+')
    result.write(protein_file)
    dna_file.close()
    codon_file.close()
    result.close()
    return protein
