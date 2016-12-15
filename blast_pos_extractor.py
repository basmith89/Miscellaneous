__author__ = 'briansmith'

import csv
import os.path
import sys
import argparse, textwrap




#####################
###File & User I/O###
#####################
parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
    description = textwrap.dedent('''\
                                 Author: Brian A. Smith
                                 University of Arizona
                                 basmith@email.arizona.edu


                                 This simple script will extract nucletoides in a contig file using BLAST cordinates.
                                 It does this by taking in an ordered csv BLAST file and searches
                                 a contigs file to extract the sequence found at the location indicated
                                 by the blast file. Note: The ordered BLAST, is only necessary if
                                 you wish the extracted sequence to be in the order to which BLAST aligned them to
                                 the reference used.'''))

parser.add_argument("-c", "--contig_file", required = True,
                    help = "Input file containing fasta contigs")
parser.add_argument("-b", "--blast_file", required = True,
                    help = "Input BLAST file in csv format")
parser.add_argument("-o", "--out_file", required = True,
                    help = "Name the output file")
args = parser.parse_args()

blast_input = open(args.blast_file, 'r')
blast_in = csv.reader(blast_input, delimiter=',')
out_file = open(args.out_file, 'a')


#To Do:
#I need to parse new lines from contig file first###
#could bring the awk statement in here and ask user to use if necessary
#I could also ensure that the blast output is sorted correctly via unix sort.  Otherwise this program is useless
#Need to figure out how to avoid N gaps. Should I just manually delete?

#Create the header line of assembly
#Change this to use blast ID for this line
#out_file.write(">Pseudomonas stutzeri DBL408_4B pMPPla107\n")

start = 0
end = 0
hit_num = 1
for row in blast_in:
    #need to reopen the file each loop here, else it is consumed in one iteration
    #and only the first provided contig line information would be spliced
    contig_input = open(args.contig_file, 'r')
    contig_id = row[1]
    start = int(row[8])
    end = int(row[9])
    qstart = int(row[6])
    qend =int(row[7])

    # debugging
    # print start
    # print end
    if start < end:
        for current_line in contig_input:
            if ">"+contig_id in current_line:
                out_file.write(">Blast Hit " + str(hit_num) + "\n")
                out_file.write(contig_input.next()[start:end] + "\n")
    elif start > end:
        for current_line in contig_input:
            if ">"+contig_id in current_line:
                out_file.write(">Blast Hit " + str(hit_num) + "\n")
                out_file.write(contig_input.next()[end:start] + "\n")
    hit_num += 1


print "Done."

