#!/usr/bin/env python

import argparse, textwrap

parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
    description = textwrap.dedent('''\
                                 Author: Brian A. Smith
                                 University of Arizona
                                 basmith@email.arizona.edu
				
				 This script was made to modify prokka output 
				 for usage with Traitar.  An identifer of choice
				 is added to each identifer line as required by Traitar format'''))
parser.add_argument("-i", "--input", required = True,
		   help = "FASTA Amino Acids file required")
parser.add_argument("-a", "--add_id", required = True,
		   help = "String identifier to be added")
parser.add_argument("-o", "--output", required = True,
		   help = "Desierd output file name")

args = parser.parse_args()

file = open(args.input, 'r')
out_file = open(args.output, 'w')
#with open(args.input, 'r+') as file:

with open(args.input, 'r') as f:
	for line in f:
		read_data = line

#with open(args.input, 'w') as f:
	for line in file.readlines():
		if line.startswith(">"):
			line = line.strip('\n') + "\t"+args.add_id+"\n"
			out_file.write(line)
		elif not line.startswith(">"):
			out_file.write(line)
file.close()  	
