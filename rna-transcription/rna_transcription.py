import functools, re

DNA2RNA = { 'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}


## decorator
def check_arg(fn):
    @functools.wraps(fn)
    def wrapped_fn(*args, **kwargs):
        (dna_strand,) = args
        if dna_strand == '': return ''
        if not re.match(r'\A[ACGT]+\Z', dna_strand):
            raise ValueError('Not a valid DNA strand')
        return fn(*args, **kwargs)
        
    return wrapped_fn


@check_arg
def to_rna_v1(dna_strand:str) -> str:
    return ''.join(map(lambda s: DNA2RNA[s],
                       dna_strand))
@check_arg
def to_rna(dna_strand:str) -> str:
    ## map
    return ''.join([DNA2RNA[s] for s in dna_strand])
