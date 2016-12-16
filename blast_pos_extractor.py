__author__ = 'briansmith'

import csv
import argparse, textwrap
import os.path
import sys

#To Do:
#I need to parse new lines from contig file first###
#could bring the awk statement in here and ask user to use if necessary

#Create the header line of assembly
#Change this to use blast ID for this line
#out_file.write(">Pseudomonas stutzeri DBL408_4B pMPPla107\n")


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
parser.add_argument("-s", "--single_contig",
                    help = "This option will create a single contig in order provided within BLAST file. "
                           "Provide an argument to name fasta header")
args = parser.parse_args()

if os.path.exists(args.out_file) and os.path.getsize(args.out_file) > 1:
    file_input = raw_input('This file already exists, do you want to overwrite it? (y/n): ')
    if file_input == "y":
        os.remove(args.out_file)
    elif file_input == "n":
        sys.exit("Exiting...")
    else:
        sys.exit("You did not provide a proper answer.  Exiting...")

blast_input = open(args.blast_file, 'r')
blast_in = csv.reader(blast_input, delimiter=',')
out_file = open(args.out_file, 'a')



def indv_hits():
    hit_num = 1
    for row in blast_in:
        #need to reopen the file each loop here, else it is consumed in one iteration
        #and only the first provided contig line information would be spliced
        contig_input = open(args.contig_file, 'r')
        contig_id = row[1]
        start = int(row[8])
        end = int(row[9])




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


def single_contig():
    out_file.write(">" + args.single_contig + "\n")
    for row in blast_in:
            #need to reopen the file each loop here, else it is consumed in one iteration
            #and only the first provided contig line information would be spliced
            contig_input = open(args.contig_file, 'r')
            contig_id = row[1]
            start = int(row[8])
            end = int(row[9])
            if start < end:
                for current_line in contig_input:
                    if ">"+contig_id in current_line:
                        out_file.write(contig_input.next()[start:end])
            elif start > end:
                for current_line in contig_input:
                    if ">"+contig_id in current_line:
                        out_file.write(contig_input.next()[end:start])

if args.single_contig:
    single_contig()
else:
    indv_hits()

print "Done."

