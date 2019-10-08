#!/usr/bin/env python

import argparse, textwrap
import re

parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
    description = textwrap.dedent('''\
                                 Author: Brian A. Smith
                                 University of Arizona
                                 basmith@email.arizona.edu
                 Trims a list of fasta headers to accession ids.
                 It is possible to maintain fasta format or output
                 ids only.'''))
parser.add_argument("-i", "--input", required = True,
           help = "sequece names file, or fasta file")
parser.add_argument("-o", "--output", required = True,
           help = "Desired output file name")
parser.add_argument("-r", "--remove_info", required = False,
           action = 'store_true', help = "Will remove info after accesion ID and keep sequece")
parser.add_argument("-I", "--id_only", required = False,
           action = 'store_true', help = "Requires only header line of fasta, will output accesion ids")

args = parser.parse_args()

file = open(args.input, 'r')
out_file = open(args.output, 'w')
fh = file.readlines()

for line in fh:
	#Removes info after accesion ID and keeps seq
	if args.remove_info == True and args.id_only == False:
		if line.startswith(">"):
			seq_id = str(line.split()[0])
			out_file.write(seq_id + "\n")
		else:
			out_file.write(line)

	#used for seq id only, input should only be fasta header lines
	####I primarly designed this for parsing info from selected sequence headers
	####from a much larger data set (ie. with grep 'strain name' [file])
	elif args.id_only == True and args.remove_info == False:
		for line in fh: 
			full_id = str(line.split()[0]) #edit out split here if all fa header info desired
			trim_id = re.sub('[>]', '', full_id)
			out_file.write(trim_id + "\n")
	else:
		print("Error: No option selected. Please select which option to perform.")
		break
		



