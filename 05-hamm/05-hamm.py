# Problem 05: http://rosalind.info/problems/hamm/
#

import os



def main():
    print(os.getcwd())
    dir = "05-hamm"
    # inputFile = f'{dir}/sample_dataset.txt'

    inputFile = f'{dir}/rosalind_hamm.txt'
    outputFile = f'{dir}/output.txt'
    with open(inputFile) as f:
        lines = f.read().splitlines()
    
    s1,s2 = lines[0],lines[1]
    diff = sum([1 if (a!=b) else 0 for a,b in zip(s1,s2)])
    print(diff)
    # input = lines[0]

    # symDict = {'A':'T','T':'A','C':'G','G':'C'}
    # print(f'Input: \n{input}')
    # output = ''.join([symDict[s] for s in input])[::-1]
    # print(output)
    # f = open(outputFile,"w")
    # f.write(output)
    # f.close()


if __name__ == "__main__":
    main()
