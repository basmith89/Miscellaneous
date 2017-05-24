__author__ = 'briansmith'
#!/usr/bin/env python

import argparse, textwrap

parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
    description = textwrap.dedent('''\
                                 Author: Brian A. Smith
                                 University of Arizona
                                 basmith@email.arizona.edu

                 This script will reverse complement a nucleotide FASTA file.'''))
parser.add_argument("-i", "--input", required = True,
           help = "FASTA file required")
parser.add_argument("-o", "--output", required = True,
           help = "Desired output file name")

args = parser.parse_args()

file = open(args.input, 'r')
out_file = open(args.output, 'w')


with open(args.input, 'r') as f:
    for line in f:
        read_data = line

    for line in file.readlines():
        if line.startswith(">"):
            out_file.write(line)
        elif not line.startswith(">"):
            line = line.strip('\n')
            seq = line

def complement(seq):
    #Reverse and complement DNA strand
    basecomplement = {'A': 'T', 'C': 'G', 'T': 'A', 'G': 'C',}
    bases = list(seq) #creates a list of bases from seq stored in bases
    #get function returns defualt type None.  Base set as default avoids KeyError Non-ACTG nucleotides
    bases = [basecomplement.get(base, base) for base in bases]
    return ''.join(bases)

#Reverse seq with list slicing method
out_file.write(complement(seq)[::-1]+ "\n")
