import re
from typing import List


def grep(pattern, flags: str, files: List[str]) -> str:
    # assume pattern to be a string or regexp
    #
    # deal with option:
    #  -n Print the line numbers of each matching line.                           => ln
    #  -l Print only the names of files that contain at least one matching line   => fn
    #  -i Match line using a case-insensitive comparison.                         => global
    #  -v Invert the program -- collect all lines that fail to match the pattern  => inv
    #  -x Only match entire lines, instead of lines that contain a match.         => fl
    #
    # TODO : regexp search

    lflags = list(set(re.split(r"\s+",
                               flags)))  # eliminate duplicate
    many_swithes = False

    if '-l' in lflags: # -l takes precedence over any other flags
        flags = '-l'
        if len(lflags) > 1:
            many_swithes = True
        proc_fn = process_file_with_fn_only

    else:
        DISPATCH = {
            '': process_file,
            'i': process_file,
            'x': process_file_with_fl, # fl == full_line
            'l': process_file_with_fn_only,
            'n': process_file_with_ln,
            'v': process_file_inv,

            'nvx': process_file_inv_fl_ln,
            'nx': process_file_with_fl_ln,
            'vx': process_file_inv_fl,
            'nv': process_file_inv_ln,
        }

        ## examples:
        ##  "-x -v -n" => "nvx",
        ##  "-v -n"    => "nv",
        ##  "-x -i -n" => "nx"
        key = "".join(
            sorted([
                x.replace('-', '') for x in filter(lambda e: e != '-i', lflags)
            ])
        )
        proc_fn = DISPATCH.get(key, None)
        if proc_fn is None:
            raise ValueError(f"Combination of options not yet managed: {key}")

    if many_swithes: flags = " ".join(lflags)

    if '-i' in  re.split(r"\s+", flags):
        pattern = pattern.lower()

    if len(files) > 1:
        matches = {f: [] for f in files}
        for f in files:
            proc_fn(pattern, lflags, f, matches[f])

        if '-l' in lflags:
            res = [
                f"{f}\n" for f in files if len(matches[f]) > 0
            ]
        else:
            res = [
                f"{f}:{l}" for f in files if len(matches[f]) > 0 for l in matches[f]
            ]
        return "".join(res)

    else:
        matches = []
        proc_fn(pattern, lflags, files[0], matches)
        return ''.join(matches)


def process_file(pattern, flags, ifile, matches):
    "default"
    assert '' in flags or '-i' in flags
    with open(ifile, "r") as fh:
        for line in fh:
            cline = line.lower() if '-i' in flags else line
            if cline.find(pattern) != -1:
                matches.append(line)
        #
        #elif '-n' in flags:
        #    for ix, line in enumerate(fh):
        #        cline = line.lower() if '-i' in flags else line
        #        if cline.find(pattern) != -1:
        #            matches.append(f"{ix + 1}:{line}")
    return


def process_file_with_ln(pattern, flags, ifile, matches):
    "with line numbers..."
    assert '-n' in flags or '-i' in flags

    with open(ifile, "r") as fh:
        for ix, line in enumerate(fh, 1):
            cline = line.lower() if '-i' in flags else line
            if line.find(pattern) != -1:
                matches.append(f"{ix}:{line}")
    return


def process_file_with_fn_only(pattern, flags, ifile, matches):
    assert '-l' in flags or '-i' in lflags
    with open(ifile, "r") as fh:
        for line in fh:
            cline = line.lower() if '-i' in flags else line

            if line.find(pattern) != -1:
                matches.append(ifile + '\n')
                break
    return


def process_file_with_fl(pattern, flags, ifile, matches):
    assert '-l' in flags or '-i' in flags or '-x' in flags
    with open(ifile, "r") as fh:
        # "with line number, and case insensitive..."
        for ix, line in enumerate(fh, 1):
            cline = line.lower() if '-i' in flags else line

            if pattern == cline[0:-1]:
                matches.append(f"{ix}:{line}" if '-n' in flags else line)
    return


def process_file_inv(pattern, flags, ifile, matches):
    "inverted search/match"
    assert "-v" in flags or "-i" in flags
    with open(ifile, "r") as fh:
        if len(flags) == 0 or '-n' not in flags:
            for line in fh:
                cline = line.lower() if '-i' in flags else line
                if cline.find(pattern) == -1:
                    matches.append(line)
    return


def process_file_inv_fl_ln(pattern, flags, ifile, matches):
    pass


def process_file_with_fl_ln(pattern, flags, ifile, matches):
    # full line match + line number
    with open(ifile, "r") as fh:
        # with fn and ln
        for ix, line in enumerate(fh, 1):
            cline = line.lower() if '-i' in flags else line

            if pattern == cline[0:-1]:
                matches.append(f"{ix}:{line}" if '-n' in flags else line)
        pass
    pass


def process_file_inv_fl(pattern, flags, ifile, matches):
    assert '-x' in flags and '-v' in flags
    with open(ifile, "r") as fh:
        for line in fh:
            cline = line.lower() if '-i' in flags else line
            if pattern != cline[0:-1]:
                matches.append(line)
    print(f"\t{matches}")
    return


def process_file_inv_ln(pattern, flags, ifile, matches):
    pass
