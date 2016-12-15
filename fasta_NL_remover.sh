awk '!/^>/ { printf "%s", $0; n = "\n" } /^>/ { print n $0; n = "" } END { printf "%s", n }'\
 contigs_4b.fasta > 408_4Bcontigs_NL_parsed.fasta