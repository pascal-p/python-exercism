import re
from typing import List


def grep(pattern: str, flags: str, files: List[str]) -> str:
    #
    # assume pattern to be a string (or regexp)
    #
    # deal with option:
    #  -l Print only the names of files that contain at least one matching line (first match)
    #
    #  -n Print the line numbers of each matching line.
    #  -v Invert the program -- collect all lines that fail to match the pattern
    #
    #  -e use regular expression pattern matching
    #
    #  -i Match line using a case-insensitive comparison.
    #  -x Only match entire lines, instead of lines that contain a match.
    #

    lflags = list(set(re.split(r"\s+",
                               flags)))  # eliminate duplicate

    if '-e' in lflags:
        pattern = re.compile(pattern)
        proc_fn = eprocess_file

    else:
        if '-i' in lflags:
            pattern = pattern.lower()

        if '-x' in lflags:
            pattern = pattern + "\n" # for full match

        proc_fn = process_file

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
                f"{f}:{l}" for f in files if len(matches[f]) > 0 \
                for l in matches[f]
            ]
        return "".join(res)

    else:
        matches = []
        proc_fn(pattern, lflags, files[0], matches)
        return ''.join(matches)


def eprocess_file(pattern: str, flags: List[str], ifile: str, matches: List[str]):
    assert type(pattern) == re.Pattern

    args = [flags, ifile, matches]
    RE_OPTS = 0
    if '-i' in flags: RE_OPTS = re.IGNORECASE;

    with open(ifile, "r") as fh:
        for ix, line in enumerate(fh, 1):

            if re.search(pattern, line, flags=RE_OPTS):
                if '-v' in flags: continue

                can_stop = add_line(ix, line, *args)
                if can_stop: break

            else:
                if '-v' in flags:
                    can_stop = add_line(ix, line, *args)
                    if can_stop: break

    return

def process_file(pattern: str, flags: List[str], ifile: str, matches: List[str]):
    args = [flags, ifile, matches]
    ##
    with open(ifile, "r") as fh:
        for ix, line in enumerate(fh, 1):
            cline = line.lower() if '-i' in flags else line

            if cline.find(pattern) == -1:  # no match
                if '-v' in flags:
                    can_stop = add_line(ix, line, *args)
                    if can_stop: break
            else:                          # match
                if '-v' in flags: continue

                can_stop = add_line(ix, line, *args)
                if can_stop: break
    return


def add_line(ix: int, line: str, flags: List[str], ifile: str,
             matches: List[str]):
    can_stop = False

    ## order matters here, as -l takes precedence over any other flags
    if '-l' in flags:
        matches.append(ifile + '\n')
        can_stop = True

    elif '-n' in flags:
        matches.append(f"{ix}:{line}")

    else:
        matches.append(line)

    return can_stop
