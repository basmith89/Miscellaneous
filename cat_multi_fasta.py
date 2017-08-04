#!/usr/bin/env python
__author__ = 'briansmith'



import argparse, textwrap

parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
    description = textwrap.dedent('''\
                                 Author: Brian A. Smith
                                 University of Arizona
                                 basmith@email.arizona.edu

                 Merges multi fasta file (contigs/scaffolds, etc) into
                 one sequence with 5 N's as spacers.'''))
parser.add_argument("-i", "--input", required = True,
           help = "FASTA file required")
parser.add_argument("-o", "--output", required = True,
           help = "Desired output file name")


args = parser.parse_args()

in_file = open(args.input, 'r')
out_file = open(args.output + ".fa", 'w')

out_file.write(">" + args.output + "\n")

#added line count to avoid adding "NNNNN" at the very beginning of seq
line_count = 0
for line in in_file.readlines():
        line = line.strip()
        if not line.startswith(">"):
            out_file.write(line)
        elif line.startswith(">") and line_count > 1:
            out_file.write("NNNNN")
        line_count += 1

out_file.write("\n")

