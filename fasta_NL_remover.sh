awk '!/^>/ { printf "%s", $0; n = "\n" } /^>/ { print n $0; n = "" } END { printf "%s", n }'\
 lac107_pMP_new.fasta > 4lac107_pMP_new_NL_parsed.fasta
