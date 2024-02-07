def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError('Strands must be of equal length.')

    hamming = 0

    for index in range(len(strand_a)):
        if strand_a[index] != strand_b[index]:
            hamming += 1

    return hamming


if __name__ == '__main__':
    print(distance('GAGCCTACTAACGGGAT', 'CATCGTAATGACGGCCT'))
