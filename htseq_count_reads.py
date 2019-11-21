import HTSeq
import collections

gtf_file = HTSeq.GFF_Reader("p_stutzeri_28a24_and_pMPPla107.gtf")
cds = HTSeq.GenomicArrayOfSets("auto", stranded=True)

for feature in gtf_file:
    if feature.type == "CDS":
        cds[feature.iv] += feature.attr["gene_id"]

almnt_file = HTSeq.BAM_Reader('pair.386_48hr_a_AATGTTGC_starAligned.out.bam')
counts = collections.Counter()

for bundle in HTSeq.pair_SAM_alignments(almnt_file, bundle =True):
    if len(bundle) != 1:
        continue # Skip multiple alignments
    first_almnt, second_almnt = bundle[0] #extract pair
    if not first_almnt.aligned and second_almnt.aligned:
        count["_unmapped"] += 1
        continue
    gene_ids = set()
    for iv, val in features[left_almnt.iv].steps():
        gene_ids |= val
    for iv, val in features[right_almnt.iv].steps():
        gene_ids |= val
    if len(gene_ids) == 1:
        gene_id = list(gene_ids)[0]
        counts[gene_id] += 1
    elif len(gene_ids) == 0:
        counts["_no_feature"] += 1
    else:
        counts["_ambiguous"] += 1

for gene_id in counts:
    print gene_id, counts[gene_id]
