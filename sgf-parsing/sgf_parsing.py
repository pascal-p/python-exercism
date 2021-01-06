import re

EOF = '@'
# STATES = { 1: 'INIT', 2: 'PREKEY', 3: 'KEY',
#            4: 'PREVALUE', 5: 'VALUE', 6: 'KV_READ',
#            7: 'DONE' }

class SgfTree:

    def __init__(self, properties=None, children=None):
        self.properties = properties or {}
        self.children = children or []

    def __eq__(self, other):
        if not isinstance(other, SgfTree):
            return False

        for k, v in self.properties.items():
            if k not in other.properties:
                return False
            if other.properties[k] != v:
                return False

        for k in other.properties.keys():
            if k not in self.properties:
                return False

        if len(self.children) != len(other.children):
            return False

        for a, b in zip(self.children, other.children):
            if a != b:
                return False

        return True

    def __ne__(self, other):
        return not self == other


class Parser:

    def __init__(self, input_string):
        self.input_string = input_string
        self.lim = len(input_string)
        # state
        self.ix, self.ch = 0, ''
        self.state = 'INIT'   # ['INIT' -> 'PREKEY' -> 'KEY' -> 'PREVALUE' -> 'VALUE' -> 'KV_READ' -> 'DONE']
        self.ds = 'PROPS'     # or 'CHILDREN'
        self.props = {}
        self.children = []

    def parse(self):
        assert self.input_string[0] == '(' and self.input_string[-1] == ')'
        ckey, cval = '', ''
        state_changed = False

        while True:
            if self.state == 'INIT':
                self.init_state_fn()
                if self.state == 'DONE': break

            if self.state == 'PREKEY':
                self.next_char()
                if self.ch == EOF:
                    return SgfTree(properties=self.props, children=self.children)

            (ckey, state_changed) = self.pre_key_state_fn(ckey, state_changed)

            if state_changed:
                self.next_char()
                state_changed = False
                if self.ch == EOF:
                    if self.state == 'DONE': break
                    else: raise(ValueError(f'Unexpected EOF'))

            ckey = self.key_state_fn(ckey)

            assert self.state == 'PREVALUE'  ## and we have a ckey, now expecting a value (cval)!

            if self.ch == '[':
                self.state = 'VALUE'
                self.next_char(raise_ex=True)
            else:
                raise(ValueError(f'Unexpected character'))

            cval = self.value_state_fn(cval)

            assert self.state == 'KV_READ'
            (ckey, cval) = self.update_tree(ckey, cval)  ## we have a ckey/cval pair - record it and prep. for next value
            (state_changed, ckey) = self.dispatch(state_changed, ckey)
            if self.state == 'DONE': break
        ##
        assert self.state == 'DONE'
        sgf = SgfTree(properties=self.props, children=self.children)
        return sgf

    def init_state_fn(self):
        self.next_char()
        if self.ch == EOF:
            self.state = 'DONE'
            return
        ##
        if self.ch != ';': raise(ValueError(f'Expected ; - got {self.ch}'))
        self.state = 'PREKEY'

    def pre_key_state_fn(self, ckey, state_changed):
        while self.state == 'PREKEY':
            # print(f'\tSTATE: {self.state} / ch: {self.ch} / ix: {self.ix} ==> ckey: {ckey}')
            if 'A' <= self.ch <= 'Z':
                ckey += self.ch
                self.state = 'KEY'
            elif self.ch == ')' and self.ix == self.lim - 1:
                self.state = 'DONE'
            else:
                raise(ValueError(f'Unexpected character 1 - got {self.ch}'))

            state_changed = True
        ##
        return (ckey, state_changed)

    def key_state_fn(self, ckey):
        while self.state == 'KEY':
            # print(f'\tSTATE: {self.state} / ch is: {self.ch} / ix: {self.ix} / key: {ckey}')
            if 'A' <= self.ch <= 'Z':
                ckey += self.ch
                self.next_char(raise_ex=True)
            elif self.ch == '[':
                self.state = 'PREVALUE'
            else:
                raise(ValueError(f'Unexpected character'))
        ##
        return ckey

    def value_state_fn(self, cval):
        while self.state == 'VALUE':
            # print(f'\tSTATE: {self.state} / ch is: {self.ch} / ix: {self.ix} / val: {cval}')
            if re.match('[a-z0-9\n]', self.ch, re.IGNORECASE):
                cval += self.ch
            elif re.match('[\s\t]', self.ch, re.IGNORECASE):
                cval += ' '
            elif self.ch == '\\':      ## escape sequence
                self.next_char(raise_ex=True)
                cval += self.ch
            elif self.ch == ']':
                self.state = 'KV_READ'
                break
            else:
                raise(ValueError(f'Unexpected character'))
            ##
            ## for next iteration
            self.next_char(raise_ex=True)
        ##
        return cval

    def dispatch(self, state_changed, ckey):
        self.next_char()
        if self.ch == EOF:
            return SgfTree(properties=self.props, children=self.children) # what we have so far

        if self.ch == '[':
            self.state = 'PREVALUE'      ## goto 'PREVALUE'

        elif 'A' <= self.ch <= 'Z':
            ckey = self.ch
            state_changed = True
            self.state = 'KEY'           ## goto 'KEY'

        elif self.ch == ';':
            self.ds = 'CHILDREN'         ## and this forevermore
            ckey = ''
            self.state = 'PREKEY'        ## goto 'PREKEY'

        elif self.ch == '(':
            self.ds = 'CHILDREN'         ## and this forevermore
            ckey = ''
            self.state = 'INIT'          ## goto 'INIT'

        elif self.ch == ')':
            if self.ix == self.lim - 1:
                self.state = 'DONE'
            else:
                self.next_char()
                if self.ch == EOF: raise(ValueError(f'Unexpected EOF'))
                ## 2 cases
                if self.ch == '(':
                    ckey = ''
                    self.state = 'INIT'  ## goto 'INIT'
                elif self.ch == ')':
                    self.state = 'DONE'
                else:
                    raise(ValueError(f'Unexpected character'))
        else:
            raise(ValueError(f'Unexpected character'))
        #
        return (state_changed, ckey)

    def update_tree(self, ckey, cval):
        if self.ds == 'PROPS':
            if ckey in self.props:
                self.props[ckey].append(cval)
            else:
                self.props[ckey] = [cval]
        else:
            assert self.ds == 'CHILDREN'   ## + assert ckey and cval available
            self.children.append(SgfTree({ckey: [cval]}))
            ckey =''
        cval = ''
        return (ckey, cval)

    def next_char(self, raise_ex=False):
        self.ix += 1
        if self.ix < self.lim:
            self.ch = self.input_string[self.ix]
            # print(f"-- Next char (ch:{self.ch} / len(ch): {len(self.ch)} / ix:{self.ix}) / {self.input_string[self.ix:-1]}")
        else:
            self.ch = EOF
            if raise_ex: raise(ValueError(f'Unexpected EOF'))


# --------------------------

def parse(input_string):
    if len(input_string) <= 0:
        raise(ValueError("Empty string"))

    # len(input) > 0
    if len(input_string) == 1:
        raise(ValueError("Invalid single character"))

    # len(input) > 1
    if len(input_string) == 2 and input_string == '()':
        raise(ValueError("Empty Expression"))

    if input_string[0] != '(' or input_string[-1] != ')':
        raise(ValueError("Not a proper expression"))

    parser = Parser(input_string)
    return parser.parse()
