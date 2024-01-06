def to_rna(dna_strand):
    trans_map = {'G': 'C', 'C': 'G',
                 'T': 'A', 'A': 'U'}
    rna = ''
    for letter in dna_strand:
        rna = rna + trans_map.get(letter.upper())

    return rna
