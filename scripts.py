from Bio.SeqUtils.ProtParam import ProteinAnalysis
import pandas as pd

def extract_features(sequence):
    """
    Takes a single amino acid string.
    Returns a pandas series containing Molecular Weight, pI, GRAVY, and Instability index)
    """
    analyzer = ProteinAnalysis(sequence)

    weight = analyzer.molecular_weight()
    pi = analyzer.isoelectric_point()
    gravy = analyzer.gravy()
    instability = analyzer.instability_index()

    return pd.Series([weight, pi, gravy, instability])