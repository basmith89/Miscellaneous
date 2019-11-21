#!/usr/bin/python
import subprocess
#This script will loop through a file with file name prefixes and send this to a PBS submission script

#input_file = open("test_sample_names.txt", "r")

with open("sample_names.txt", "rb") as infile:
    for line in infile: 
        line = line.strip("\n")
    #sample
    #print line #debug line for calling file names
        #Create directory for each sample
        create_dir = "mkdir star_aligned/"+line
        subprocess.call(create_dir, shell =True)
        qsub_cmd = "qsub -v SAMPLE=" + line + " star_pbs.sh"
        #print qsub_cmd
        exit_status = subprocess.call(qsub_cmd, shell=True)
        if exit_status is 1:
            print "Job" + line + " failed to submit".format(qsub_cmd)
print "Done. Submitting jobs."
