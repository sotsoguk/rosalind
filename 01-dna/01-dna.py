# Problem 01: DNA
# http://rosalind.info/problems/dna/

import os
from collections import Counter

def main():
    print(os.getcwd())
    #inputFile = f'sample_dataset'
    inputFile = f'rosalind_dna.txt'
    with open(inputFile) as f:
        lines = f.read().splitlines()
    input = lines[0]
    print(input)
    c = Counter(input)
    output = f"{c['A']} {c['C']} {c['G']} {c['T']}"
    print(output)
    

    

    return 0

if __name__ == "__main__":
    main()