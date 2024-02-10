DNA_TO_RNA_TABLE = str.maketrans("GCTA", "CGAU")

def to_rna(dna_strand):
    return dna_strand.translate(DNA_TO_RNA_TABLE)
