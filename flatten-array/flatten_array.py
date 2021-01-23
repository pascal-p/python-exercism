def flatten(iterable):
    nlst = []
    #
    for item in iterable:
        if item is None:
            continue
        elif isinstance(item, list):
            nlst.extend(flatten(item))
        else:
            nlst.append(item)
    #
    return nlst
