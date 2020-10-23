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
    #  -i Match line using a case-insensitive comparison.
    #  -x Only match entire lines, instead of lines that contain a match.
    #
    # TODO: regexp search with -e

    lflags = list(set(re.split(r"\s+",
                               flags)))  # eliminate duplicate
    if '-i' in lflags: 
        pattern = pattern.lower()

    if '-x' in lflags:
        pattern = pattern + "\n" # for full match
        
    if len(files) > 1:
        matches = {f: [] for f in files}
        for f in files:
            process_file(pattern, lflags, f, matches[f])

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
        process_file(pattern, lflags, files[0], matches)
        return ''.join(matches)


def process_file(pattern: str, flags: List[str], ifile: str,
                 matches: List[str]):
    ## closure
    def add_line(ix, line):
        can_stop = False

        # order matters here, as -l takes precedence over any other flags
        if '-l' in flags:
            matches.append(ifile + '\n')
            can_stop = True
    
        elif '-n' in flags:
            matches.append(f"{ix}:{line}")
            
        else:
            matches.append(line)
            
        return can_stop

    ## 
    with open(ifile, "r") as fh:
        for ix, line in enumerate(fh, 1):
            cline = line.lower() if '-i' in flags else line

            if cline.find(pattern) == -1:  # no match
                if '-v' in flags:
                    can_stop = add_line(ix, line)
                    if can_stop: break    
            else:                          # match
                if '-v' in flags: continue
                
                can_stop = add_line(ix, line)
                if can_stop: break
    return



