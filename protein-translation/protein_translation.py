from enum import Enum
from textwrap import wrap


class Protein(Enum):
    METHIONINE = "Methionine"
    PHENYLALANINE = "Phenylalanine"
    LEUCINE = "Leucine"
    SERINE = "Serine"
    TYROSINE = "Tyrosine"
    CYSTEINE = "Cysteine"
    TRYPTOPHAN = "Tryptophan"
    STOP = "STOP"


CODON_TO_PROTEIN = {
    "AUG": Protein.METHIONINE,
    "UUU": Protein.PHENYLALANINE,
    "UUC": Protein.PHENYLALANINE,
    "UUA": Protein.LEUCINE,
    "UUG": Protein.LEUCINE,
    "UCU": Protein.SERINE,
    "UCC": Protein.SERINE,
    "UCA": Protein.SERINE,
    "UCG": Protein.SERINE,
    "UAU": Protein.TYROSINE,
    "UAC": Protein.TYROSINE,
    "UGU": Protein.CYSTEINE,
    "UGC": Protein.CYSTEINE,
    "UGG": Protein.TRYPTOPHAN,
    "UAA": Protein.STOP,
    "UAG": Protein.STOP,
    "UGA": Protein.STOP,
}


def proteins(strand):
    proteins = []
    for codon in wrap(strand, 3):
        protein = CODON_TO_PROTEIN[codon]
        if protein is Protein.STOP:
            break
        proteins.append(protein.value)
    return proteins
