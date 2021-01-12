def slices(series:str, length:int):

    if len(series) == 0 and length > 0:
        raise(ValueError("Empty Series"))

    if len(series) > 0 and \
       (length <= 0 or length > len(series)):
        raise(ValueError("Incompatibility"))

    return [
        series[ix:ix + length] for ix in range(0, len(series) - length + 1)
    ]
