from collections import Counter

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from Bio import SeqIO
from tqdm import tqdm

from constants import TRAIN_DIR


def read_fasta(path):
    """
    Read FASTA file and return a dataframe with the sequence IDs and sequences.
    FASTA format: https://en.wikipedia.org/wiki/FASTA_format
    - the FASTA format is a text-based format for representing either nucleotide sequences
    or amino acid (protein) sequences, in which nucleotides or amino acids are represented
    using single-letter codes
    """

    fasta_seqs = SeqIO.parse(open(path), "fasta")
    ids, seqs, descs = [], [], []

    for seq in fasta_seqs:
        ids.append(seq.id)
        seqs.append(str(seq.seq))
        descs.append(seq.description)
    return pd.DataFrame({"id": ids, "seq": seqs, "desc": descs})


if __name__ == "__main__":
    # train_df = read_fasta(TRAIN_DIR / "train_sequences.fasta")
    # print(train_df.head())

    # amino_acid_list = [amino_acid for seq in train_df["seq"] for amino_acid in seq]
    # amino_acid_count = Counter(amino_acid_list)
    # print(amino_acid_count.keys())
    # print(amino_acid_count.values())

    # Descending order of amino acid count
    # amino_acid_count = dict(
    #     sorted(amino_acid_count.items(), key=lambda x: x[1], reverse=True)
    # )
    # {'L': 7386109, 'S': 6493284, 'A': 5601393, 'E': 5388873, 'G': 5061691, 'V': 4931367,
    #  'K': 4594229, 'P': 4382337, 'T': 4378528, 'R': 4283020, 'D': 4151113, 'I': 3879567,
    #  'Q': 3563728, 'N': 3400751, 'F': 2930638, 'Y': 2239153, 'H': 1914456, 'M': 1776672,
    #  'C': 1504314, 'W': 888449, 'X': 2771, 'U': 148, 'O': 4, 'B': 4, 'Z': 4}

    """
    Notes:
    -----
    # https://www.genome.jp/kegg/catalog/codes1.html
    - The most common amino acids are L (leucine), S (serine), A (alanine), E (glutamic acid), G (glycine),
    these amino acids are often prevalent in many protein sequences because they play crucial roles in
    protein structure and function.
    - The presence of "X" could suggest that there are some sequences in the dataset with unknown or unclassified
    amino acids. These could also be placeholders for positions where the amino acid could not be determined.
    - The occurrence of "U" and "O" is relatively rare because these are not among the standard 20 amino acids
    found in most organisms. They are known as selenocysteine (U) and pyrrolysine (O) respectively, and their
    presence could suggest that the dataset includes sequences from organisms that use these unusual amino acids.
    - The presence of "B" and "Z" could suggest that the dataset includes sequences from organisms that use
    unusual amino acids. "B" is a placeholder for asparagine (N) or aspartic acid (D), while "Z" is a placeholder
    for glutamine (Q) or glutamic acid (E). They're typically used when sequencing hasn't definitively determined
    which of these two alternatives is present.
    """

    # Frequency of amino acids
    # sns.barplot(
    #     x=list(amino_acid_count.values()),
    #     y=list(amino_acid_count.keys()),
    #     color="black",
    #     orient="h",
    # )
    # plt.show()

    # Distribution of amino acid lengths
    # sns.histplot(train_df["seq"].apply(len), color="black", kde=True)
    # plt.show()

    train_terms = pd.read_csv(TRAIN_DIR / "train_terms.tsv", sep="\t")
    # print(train_terms.head())

    # Distribution of term lengths
    """
    Notes:
    -----
    BPO: Biological Process Ontology
        - A biological process is a collection of molecular events with a defined beginning and end, pertinent
        to the functioning of integrated living units: cells, tissues, organs, and organisms.
    CCO: Cellular Component Ontology
        -  The parts of a cell or its extracellular environment.
    MFO: Molecular Function Ontology
        - The elemental activities of a gene product at the molecular level, such as binding or catalysis
    """
    aspects = train_terms["aspect"].unique()
    sns.barplot(x=aspects, y=train_terms["aspect"].value_counts())
    plt.show()
