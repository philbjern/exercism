def proteins(strand):
    CODON_LEN = 3
    STOP = 'STOP'

    protein_map = {'AUG': 'Methionine',
                   'UUC': 'Phenylalanine',
                   'UUU': 'Phenylalanine',
                   'UUA': 'Leucine',
                   'UUG': 'Leucine',
                   'UCU': 'Serine',
                   'UCC': 'Serine',
                   'UCA': 'Serine',
                   'UCG': 'Serine',
                   'UAU': 'Tyrosine',
                   'UAC': 'Tyrosine',
                   'UGU': 'Cysteine',
                   'UGC': 'Cysteine',
                   'UGG': 'Tryptophan',
                   'UAA': STOP,
                   'UAG': STOP,
                   'UGA': STOP,
                   }

    seq = []
    for i in range(0, len(strand), CODON_LEN):
        seq.append(strand[i:i+CODON_LEN])

    res = []
    for codon in seq:
        if protein_map[codon] == STOP:
            break

        res.append(protein_map[codon])

    return res
