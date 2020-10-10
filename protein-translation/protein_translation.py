from typing import List

# CODON => PROTEIN
COD_PRO = {
    'AUG': 'Methionine',
    'UUU': 'Phenylalanine', 'UUC': 'Phenylalanine',
    'UUA': 'Leucine', 'UUG': 'Leucine',
    'UCU': 'Serine', 'UCC': 'Serine', 'UCA': 'Serine', 'UCG': 'Serine',
    'UAU': 'Tyrosine', 'UAC': 'Tyrosine',
    'UGU': 'Cysteine', 'UGC': 'Cysteine',
    'UGG': 'Tryptophan',
    'UAA': 'STOP', 'UAG': 'STOP', 'UGA': 'STOP',
}

LEN_COD = 3

def proteins(strand: str) -> List[str]:
    strand = strand.upper()

    if len(strand) == LEN_COD:
        val = get_value(strand)
        return [] if val is None else [val]

    if len(strand) % 3 != 0:
        raise KeyError("Not such CODON in our base (yet)...")

    proteins = []
    for ix in range(0, len(strand), LEN_COD):
        val = get_value(strand[ix:(ix + LEN_COD)])
        if val is None: return proteins
        proteins.append(val)

    return proteins

def get_value(key):
    if key in COD_PRO.keys():
        val = COD_PRO[key]
        if val == 'STOP': val = None
        return val
    raise KeyError("Not such CODON in our base (yet)...")
