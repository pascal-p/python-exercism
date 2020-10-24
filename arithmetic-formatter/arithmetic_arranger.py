from typing import List
import re

SPC = " " * 4
NUM_LEN, NUM_LEM_STR = 6, "six"
NUM_EXPR = 5
OP_ALLOWED = ['+', '-', 'x']
#
# arithmetic expression are composed of integers with artihemtic operators:
# + or -
#
# no limitation on the isze of numbers?
# ARITH_EXPR = r"\b\d{1," + str(NUM_LEN) + r"}\s+[\-\+]{1}\s+\d{1," + str(NUM_LEN) + r"}\b"

def arithmetic_arranger(problems: List[str], show_sol=False) -> str:
    # expr = re.compile(ARITH_EXPR)

    top_line, bot_line, sep = [], [], []
    if show_sol: sol = []

    rexpr = re.compile(r"\b\d{1," + str(NUM_LEN) + r"}\b")

    for p in problems:
        if 'x' in p:
            return mult_arranger(problems, show_sol)

    try:
        if len(problems) > NUM_EXPR:
            raise ValueError("Error: Too many problems.")

        for p in problems:
            # if not re.match(expr, p):
            #    raise ValueError(f"Not an acceptable arithmetic expression: <{p}>")

            ## split + calc. len
            (oper1, op, oper2) = re.sub(r"\s+", ' ', p).split(" ")

            if op not in OP_ALLOWED:
                raise ValueError(f"Error: Operator must be '{OP_ALLOWED[0]}' or '{OP_ALLOWED[1]}' or '{OP_ALLOWED[2]}'.")

            if len(oper1) > NUM_LEN or len(oper2) > NUM_LEN:
                raise ValueError(f"Error: Numbers cannot be more than {NUM_LEM_STR} digits.")

            for oper in (oper1, oper2):
                if not re.match(rexpr, oper):
                    raise ValueError("Error: Numbers must only contain digits.")

            n = max([len(o) for o in (oper1, oper2)]) ## max([len(oper1), len(oper2)])
            plen = n + 2                              ## 1 spc, 1 op

            top_line.append(" " * (plen - len(oper1)) + oper1)
            bot_line.append(f"{op} " + " " * (plen -2 - len(oper2)) + oper2)
            sep.append("-" * plen)

            if show_sol:
                if op == '+':
                    res = int(oper1) + int(oper2)
                else:
                    # op == '-':
                    res = int(oper1) - int(oper2)

                sres = str(res)
                nres = len(sres)
                sol.append(" " * (plen - nres) + sres)

        s1 = SPC.join(top_line)
        s2 = SPC.join(bot_line)
        s3 = SPC.join(sep)

        if show_sol:
            s4 = SPC.join(sol)
            return f"{s1}\n{s2}\n{s3}\n{s4}"

        return f"{s1}\n{s2}\n{s3}"

    except ValueError as err:
        print("GOT ", err)
        return str(err)

def mult_arranger(problems: List[str], show_sol=False) -> str:
    # find where is the mult as it will determine the "shape of res"

    pass

def mult_inter_sol(oper1, oper2):
    oper1 = inte(oper1)

    res = [[] for _ in oper2]   # number of sub-arrays

    for n, d in enumerate(oper2):
        r = str(oper1 * d) + '.' * n
        res[n].append(r)

    pass
