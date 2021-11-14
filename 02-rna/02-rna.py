# Problem 02: http://rosalind.info/problems/rna/
# http://rosalind.info/problems/dna/

import os
from collections import Counter


def main():
    print(os.getcwd())
    # inputFile = f'02-rna/sample_dataset.txt'
    inputFile = f'02-rna/rosalind_rna.txt'
    with open(inputFile) as f:
        lines = f.read().splitlines()
    input = lines[0]
    print(f'Input: \n{input}')
    output = ''.join([ n if n in {'A','C','G'} else 'U' for n in input])
    print(output)


if __name__ == "__main__":
    main()
