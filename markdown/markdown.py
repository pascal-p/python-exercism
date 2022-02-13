"""
   Markdown exercice
"""

import re


def parse(markdown: str) -> str:
    """
       parse a markdwon input -> htl
    """
    lines = markdown.split('\n')
    res = ''
    in_list, in_list_append = False, False
    for line in lines:
        line = transform_headers(line)  # deal with headers
        m = re.match(r'\* (.*)', line)  # itemize with *
        if m:
            curr = m.group(1)
            curr = transform_bold(curr)
            curr = transform_italic(curr)
            if not in_list:  # => start a list with ul
                in_list = True
                line = '<ul><li>' + curr + '</li>'
            else:
                line = '<li>' + curr + '</li>'  # in_list => add item with li
        elif in_list:
            in_list_append, in_list = True, False
        #
        if not re.match('<h|<ul|<p|<li', line):
            line = '<p>' + line + '</p>'
        line = transform_bold(line)
        line = transform_italic(line)
        #
        if in_list_append:
            line = '</ul>' + line  # close current list
            in_list_append = False
        res += line
    if in_list:         # no more lines and we were in a state list =>
        res += '</ul>'  # close the current list
    return res


def transform_bold(line: str) -> str:
    """
       bold emphasis
    """

    m = re.match('(.*)__(.*)__(.*)', line)
    if m:
        line = m.group(1) + '<strong>' + m.group(2) + '</strong>' + m.group(3)
    return line


def transform_italic(line: str) -> str:
    """
       italic emphasis
    """
    m = re.match('(.*)_(.*)_(.*)', line)
    if m:
        line = m.group(1) + '<em>' + m.group(2) + '</em>' + m.group(3)
    return line


def transform_headers(line: str) -> str:
    """
       deal with headers
    """
    if re.match(r'######\s+', line) is not None:
        line = re.sub(r"######\s+(.*)", r"<h6>\1</h6>", line)
    elif re.match(r'#####\s+', line) is not None:
        line = re.sub(r"#####\s+(.*)", r"<h5>\1</h5>", line)
    elif re.match(r'####\s+', line) is not None:
        line = re.sub(r"####\s+(.*)", r"<h4>\1</h4>", line)
    elif re.match(r'###\s+', line) is not None:
        line = re.sub(r"###\s+(.*)", r"<h3>\1</h3>", line)
    elif re.match(r'##\s+', line) is not None:
        line = re.sub(r"##\s+(.*)", r"<h2>\1</h2>", line)
    elif re.match(r'#\s+', line) is not None:
        line = re.sub(r"#\s+(.*)", r"<h1>\1</h1>", line)
    return line
