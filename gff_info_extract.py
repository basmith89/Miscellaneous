#!/usr/bin/env python
__author__ = 'briansmith'
import csv
import re
import argparse, textwrap


###Notes
#This is a version worked on when converting .gff to .csv in the command line.  
#For some reason if using excel to convert .gff to .csv the last column is enclosed
#By quotes.  This allows another version of this script to work.
#I still have no idea why this script will not capture specific product= searches 
#such as DNA-binding protein HU, but it will capture tRNA or hypotheticals.
#I can't identify what seperates the two for regex.

parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
    description = textwrap.dedent('''\
                                 Author: Brian A. Smith
                                 University of Arizona
                                 basmith@email.arizona.edu

                 This script will extract amino acid seq ID from
                 prokka's gff3 file and the start, end position into
                 a tab delimited file.
                 NOTE: ensure there are no comment lines in input file.'''))

parser.add_argument("-i", "--input", required = True,
           help = "FASTA file required")
parser.add_argument("-o", "--output", required = True,
           help = "Desired output file name")

args = parser.parse_args()

out_file = open(args.output, 'w')

#'rU' allows to read file unversial new-line mode
with open(args.input, 'rU') as f:
    #next(f)
    readcsv = csv.reader(f, delimiter=',')
    for row in readcsv:
        seq_id = row[8]
        try:
            seq_id = re.search(r'ID=(.*?);', row[8]).group(1)
        except AttributeError:
            found = 'No match found'

        gene_name = ""
        #gene_name = row[8]
        #product_name = 0
        product_name = re.search(r';product=(.*)', row[8])
        if product_name:
             product_name = product_name.group(1)

        gene_name = re.search(r';gene=(.*?);', row[8])
        if gene_name:
            gene_name = gene_name.group(1)

        if gene_name > 0:
            desc = gene_name
        else:
            #product_name = re.findall(r"(?<=product=).+$", row[8], re.M)
            desc = str(product_name)
        startcoord = row[3]
        endcoord = row[4]
        out_file.write(seq_id + "\t" + startcoord + "\t" + endcoord + "\t" + desc + "\n")
