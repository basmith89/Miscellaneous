__author__ = 'briansmith'
#!/usr/bin/env python

import argparse, textwrap

parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
    description = textwrap.dedent('''\
                                 Author: Brian A. Smith
                                 University of Arizona
                                 basmith@email.arizona.edu

                 This script will count GC content of fasta files.
                 If multi fasta file used, it will concatenate all sequences'''))
parser.add_argument("-i", "--input", required = True,
           help = "FASTA file required")

args = parser.parse_args()

in_file = open(args.input, 'r')


nuc_list = []

for line in in_file.readlines():
        line = line.strip()
        for nuc in line:
            if not line.startswith(">"):
                #    nuc_list.append(data)
                    #print line.strip("\n") #debug statement to see output
                nuc_list.append(nuc[::1])

total = len(nuc_list)
i = 0
for n in nuc_list:
    if n == "G" or\
       n == "g" or\
       n == "C" or\
       n == "c":
        i += 1

gc_cont = float(i)/total*100
print "GC content =", gc_cont