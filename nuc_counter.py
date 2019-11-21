#!/usr/bin/python

__author__ = 'briansmith'



import argparse, textwrap


parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
    description = textwrap.dedent('''\
                                 Author: Brian A. Smith
                                 University of Arizona
                                 basmith@email.arizona.edu
                 
                 This script will count nucleotides and output to
                 a tab delmitted format'''))

parser.add_argument("-i", "--input", required = True,
           help = "FASTA file required")
parser.add_argument("-o", "--output", required = True,
           help = "Desired output name")

args = parser.parse_args()

out_file = open(args.output, "w")
nuc_count = 0

with open(args.input) as f:
	for line in f:
		if line.startswith('>'):
			seq_id = line.strip("\n") 
			#out_file.write(line)
			nuc_count = 0
		#elif line.startswith('a' or 'c' or 'g' or 't'):
		else:
			#for x in line:
			nuc_count = line.count("a") + line.count("c") + line.count("g") + line.count("t") 
			#if line == ">":
			#	break
			nuc_count = str(nuc_count)
			out_file.write(seq_id + "\t" + nuc_count + "\n")

