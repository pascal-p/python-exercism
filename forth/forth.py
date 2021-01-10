from typing import List
import re

class StackUnderflowError(Exception):
    pass


class Forth:
    ARITHMETIC_OPS = ['+', '-', '*', '/']
    STACK_OPS = ['DUP', 'DROP', 'SWAP', 'OVER']
    SYMB = [':', ';']

class StackInt:
    def __init__(self):
        self.buf = []

    def __len__(self):
        return len(self.buf)

    def push(self, elem:int):
        self.buf.append(elem)
        return self

    def pop(self):
        if len(self.buf) == 0:
            raise(StackUnderflowError("Error Empty stack"))
        elem = self.buf[-1]
        self.buf = self.buf[:-1]
        return elem

    def top(self):
        if len(self.buf) == 0:
            raise(StackUnderflowError("Error Empty stack"))
        return self.buf[-1]

    def __repr__(self):
        return f"{self.stack}"


def evaluate(input_data:List[str]):
    stack = StackInt()
    tokens_lst = tokenize(input_data)    ## Array of array of tokens?
    seen_op = False
    uenv = {}
    key, val = None, []

    for tokens in tokens_lst:
        state = 'STD'

        for token in tokens:
            if state == 'ASSIGN_KEY':
                if not is_word(token) and not(is_arithmetic_op(token)):
                    raise(ValueError(f'Not a word: {token}'))
                key = token
                state = 'ASSIGN_VAL'

            elif state == 'ASSIGN_VAL':
                if token == ';':
                    uenv[key] = val                 ## overwrite if key already present
                    state = 'STD'
                else:
                    if is_word(token) and token in uenv:
                        val.append(uenv[token][0])  ## replace token by its value!
                    else:
                        val.append(token)

            elif state == 'STD':
                if is_num(token):
                    stack.push(token)

                elif is_cust_op(token, uenv):  ## Need to be defined before is_stack_op(token) and is_arithmetic_op(token)...
                    #                          ## ... because custom action can overide (predefined) stack/arithmetic action(s)
                    cust_action_fn(token, uenv, stack)

                elif is_arithmetic_op(token):
                    seen_op = True
                    stack.push(op_fn(token, stack))

                elif is_stack_op(token):
                    action_fn(token, stack)  ## Can be unary or binary

                elif is_symbol(token):
                    state = 'ASSIGN_KEY' if token == Forth.SYMB[0] else 'STD'
                    key, val = None, []
                    # continue

                else:
                    raise(ValueError("Not a valid instruction"))
            else:
                raise(ValueError(f'Unknown state {state}'))
    #
    if seen_op:
        assert len(stack) == 1
    return stack.buf


def tokenize(input_data:List[str]):
    jx = 0
    tokens = [[] for _ in range(len(input_data))]
    for inp in input_data:
        state, ctoken  = 'init', ''

        ix = 0
        while ix < len(inp):
            ch = inp[ix]
            ix += 1
            # print(f">> state: {state} / ch: [{ch}] / inp: {inp}")
            if re.match('\s', ch, re.IGNORECASE):
                add_token(state, ctoken, tokens, jx)
                state, ctoken = 'init', ''
                # continue

            elif state == 'init':
                if '0' <= ch <= '9':
                    state = 'number'
                    ctoken = ch

                elif re.match('[a-z]', ch, re.IGNORECASE):
                    state = 'word'
                    ctoken = ch.upper()

                elif ch in Forth.ARITHMETIC_OPS:
                    state = 'op'
                    ctoken = ch

                elif ch in Forth.SYMB:
                    state = 'symbol'
                    ctoken = ch

                else:
                    raise(ValueError("Unexpected token"))

            elif state == 'number':
                if '0' <= ch <= '9':
                    ctoken += ch
                else:
                    raise(ValueError("Not a number"))

            elif state == 'op':
                ## Not expecting to read any more char for this token
                raise(ValueError("Not a supported operator"))

            elif state == 'word':
                if re.match('[a-z0-9:;\-]', ch, re.IGNORECASE):
                    ctoken += ch.upper()
                else:
                    raise(ValueError("Not a valid word"))

            elif state == 'symbol':
                ## Not expecting to read any more char for this token
                raise(ValueError("Not a supported symbol"))

            else:
                raise(ValueError(f"Invalid state / on loop over state;: {state}"))
        # end while
        add_token(state, ctoken, tokens, jx)
        jx +=1
    #
    return tokens

def add_token(state, ctoken, tokens, jx):
    if state == 'word':
        tokens[jx].append(ctoken)

    elif state == 'number':
        tokens[jx].append(int(ctoken))  ## no exception expected

    elif state == 'op':
        tokens[jx].append(ctoken)

    elif state == 'symbol':
        tokens[jx].append(ctoken)

    else:
        raise(ValueError(f"Invalid state {state}!"))

    return

def is_word(token) -> bool:
    return re.match('\A[a-z][a-z0-9:;\-]+\Z', str(token), re.IGNORECASE) is not None

def is_num(token:str) -> bool:
    return re.match('\A\d+\Z', str(token), re.IGNORECASE)

def is_arithmetic_op(token:str) -> bool:
    return token in Forth.ARITHMETIC_OPS

def is_stack_op(token:str) -> bool:
    return token in Forth.STACK_OPS

def is_cust_op(token:str, uenv) -> bool:
    return token in uenv

def is_symbol(token:str) -> bool:
    return token in Forth.SYMB

def op_fn(op:str, stack):
    y = stack.pop()
    x = stack.pop()

    if op == Forth.ARITHMETIC_OPS[0]:    # +
        return x + y
    elif op == Forth.ARITHMETIC_OPS[1]:  # -
        return x - y
    elif op == Forth.ARITHMETIC_OPS[2]:  # *
        return x * y
    elif op == Forth.ARITHMETIC_OPS[3]:  # /
        if y > 0:
            return x // y
        else:
            raise(ZeroDivisionError("Division by zero"))

def action_fn(kword:str, stack, redefined=False):
    if kword == Forth.STACK_OPS[0]:       ## DUP (unary) ...x y => ...x y y
        y = stack.top()
        stack.push(y)

    elif kword == Forth.STACK_OPS[1]:     ## DROP ...x y => ...x
        stack.pop()

    elif kword == Forth.STACK_OPS[2]:
        if not redefined:                 ## SWAP (binary) ...x y => ...y x
            y = stack.pop()
            x = stack.pop()
            stack.push(y)
            stack.push(x)
        else:                             ## SWAP redefined (unary)  ...y   => ...y y
            y = stack.top()
            stack.push(y)

    elif kword == Forth.STACK_OPS[3]:     ## OVER ...x y => ...x y x
        y = stack.pop()
        x = stack.top()                   ## to dup, hence the top() call
        stack.push(y)
        stack.push(x)

    else:
        raise(ValueError(f"{kword} not yet managed"))

    return

def cust_action_fn(kword:str, uenv, stack):
    for op in uenv[kword]:
        if is_stack_op(op):
            action_fn(op, stack, redefined=True)

        elif is_arithmetic_op(op):
            stack.push(op_fn(op, stack))

        elif re.match('\A\d+\Z', str(op)): # number
            stack.push(op)

        else:
            raise(ValueError(f'Unknown custom Operator {op}'))
    return
