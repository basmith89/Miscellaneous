__author__ = 'briansmith'

#!/usr/bin/env python

import argparse, textwrap

parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
    description = textwrap.dedent('''\
                                 Author: Brian A. Smith
                                 University of Arizona
                                 basmith@email.arizona.edu

                 Line slicing script of FASTA files
                 NOTE: step parameter has not been added.'''))
parser.add_argument("-i", "--input", required = True,
           help = "FASTA file required")
parser.add_argument("-o", "--output", required = True,
           help = "Desired output file name")
parser.add_argument("-s", "--start_slice", required = False,
                    type = int, help = "Select a starting position to cut [START:end:step]")
parser.add_argument("-e", "--end_slice", required = False,
                    type = int, help = "Select an ending position to cut [start:END:step]")

args = parser.parse_args()

file = open(args.input, 'r')
out_file = open(args.output, 'w')
#with open(args.input, 'r+') as file:

if args.start_slice:
    start_slice = args.start_slice - 1
    print start_slice

with open(args.input, 'r') as f:
    for line in f:
        read_data = line

#with open(args.input, 'w') as f:
    for line in file.readlines():
        if line.startswith(">"):
            out_file.write(line)
        elif not line.startswith(">"):
            line = line.strip('\n')
            if args.start_slice:
                out_file.write(line[start_slice:])
            elif args.end_slice:
                out_file.write(line[:args.end_slice])
            out_file.write("\n")
