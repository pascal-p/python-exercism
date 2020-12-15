SEC_HSHAKE_CODE = {1: "wink", 2: "double blink", 4: "close your eyes", 8: "jump", 16: "reverse"}

BASE = sorted([k for k in SEC_HSHAKE_CODE.keys()], reverse=True)

def commands(code:int):
    if not isinstance(code, int) or code < 0:
        raise Exception(f"code {code} msut be a non negative integer")

    if code == 0: return []

    (code, func) = case_16(code, 'insert')
    ix = 1
    actions = []
    while code >= 1:
        count = False

        if code >= BASE[ix]:
            code -= BASE[ix]
            count = True

        if count:
            action = SEC_HSHAKE_CODE[BASE[ix]]

            if func == 'insert':
                actions.insert(0, action)
            elif func == 'append':
                actions.append(action)

        ix += 1
    #
    return actions

def case_16(code:int, func:str):
    count = 0

    while code >= BASE[0]:
        code -= BASE[0]
        count += 1

    if count % 2 == 1:
        func = 'append'

    return (code, func)
