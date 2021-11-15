# Problem 04: http://rosalind.info/problems/gc/
#

import os
from collections import Counter

def FASTA_reader(input):
    d ={}
    curr_id = input[0][1:]
    curr_string = ""
    for i in range(1,len(input)):
        # comment
        if (input[i].startswith(':')):
            continue
        elif (input[i].startswith('>')):
            d[curr_id] = curr_string
            curr_id = input[i][1:]
            curr_string = ""
        else:
            curr_string += input[i]
    d[curr_id] = curr_string
    return d

def GC_content(st):
    gcs = sum([1 if s in {'G','C'} else 0 for s in st])
    return float(gcs) / float(len(st)) * 100

def main():
    print(os.getcwd())
    dir = "04-gc"
    # inputFile = f'{dir}/sample_dataset.txt'

    inputFile = f'{dir}/rosalind_gc.txt'
    outputFile = f'{dir}/output.txt'
    with open(inputFile) as f:
        lines = f.read().splitlines()
    # input = lines[0]

    d = FASTA_reader(lines)
    outD = {}
    for k,v in d.items():
        #print(f'{k}\n{v}')
        outD[k] = GC_content(v)

    # for k,v in outD.items():
    #     print(f'{k}\n{v}')

    maxGC = max(outD,key=outD.get)
    print(f'{maxGC}\n{outD[maxGC]:.6f}')
    # symDict = {'A':'T','T':'A','C':'G','G':'C'}
    # print(f'Input: \n{input}')
    # output = ''.join([symDict[s] for s in input])[::-1]
    # print(output)
    # f = open(outputFile,"w")
    # f.write(output)
    # f.close()


if __name__ == "__main__":
    main()
