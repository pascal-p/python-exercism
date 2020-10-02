import functools

#
# Assuming strands are correctly formed with only uppercase letters 'A', 'C', 'G', 'T'
# if not add: re.match(r'\A[ACGT]+\Z', strand) ...
#

## decorator
def check_len(fn):
    @functools.wraps(fn)
    def wrapped_fn(*args, **kwargs):
        (strand_a, strand_b) = args
        if len(strand_a) != len(strand_b):
            raise ValueError('strands must be of same length')
        if strand_a == '' and strand_b == '':
            return 0
        return fn(*args, **kwargs)

    return wrapped_fn

@check_len
def distance(strand_a, strand_b):
    ## with for
    return sum([x != y for x, y in zip(strand_a, strand_b)])

@check_len
def distance_v1(strand_a, strand_b):
    ## with filter
    return len(
        list(
            filter(lambda t: t[0] != t[1],
                   zip(strand_a, strand_b))
        )
    )

@check_len
def distance_v2(strand_a, strand_b):
    ## with reduce
    return functools.reduce(
        lambda cnt, t: cnt + 1 if t[0] != t[1] else cnt,
        zip(strand_a, strand_b),
        0
    )
