# Problem 03: http://rosalind.info/problems/revc/
#

import os
from collections import Counter


def main():
    print(os.getcwd())
    dir = "03-revc"
    # inputFile = f'{dir}/sample_dataset.txt'

    inputFile = f'{dir}/rosalind_revc.txt'
    outputFile = f'{dir}/output.txt'
    with open(inputFile) as f:
        lines = f.read().splitlines()
    input = lines[0]

    symDict = {'A':'T','T':'A','C':'G','G':'C'}
    print(f'Input: \n{input}')
    output = ''.join([symDict[s] for s in input])[::-1]
    print(output)
    f = open(outputFile,"w")
    f.write(output)
    f.close()


if __name__ == "__main__":
    main()
