# Problem 06: http://rosalind.info/problems/subs/
#

import os

from collections import Counter


def main():
    print(os.getcwd())
    dir = "06-subs"
    # inputFile = f'{dir}/sample_dataset.txt'
    inputFile = f'{dir}/rosalind_subs.txt'

    outputFile = f'{dir}/output.txt'
    with open(inputFile) as f:
        lines = f.read().splitlines()
    dna = lines[0]
    motif = lines[1]

    matches = []
    for i in range(len(dna)-len(motif)+1):
        if dna[i:i+len(motif)] == motif:
            matches.append(i+1)
            
    for m in matches:
        print(m,end= " ")
    print()
    # symDict = {'A':'T','T':'A','C':'G','G':'C'}
    # print(f'Input: \n{input}')
    # output = ''.join([symDict[s] for s in input])[::-1]
    # print(output)
    # f = open(outputFile,"w")
    # f.write(output)
    # f.close()


if __name__ == "__main__":
    main()
