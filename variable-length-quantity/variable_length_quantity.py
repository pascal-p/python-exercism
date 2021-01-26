from typing import List

SCALE_INP = 16  ## Hex.
SCALE_BIN = 2   ## Binary
NBITS = 32
ENC_LEN = 7
OFFSET = 4
DEBUG = 0

def encode(numbers: List[int]) -> List[int]:
    """
    1 - input base is 16
    2 - hexa -> bin string
    3 - unpack per group of 7 bits, repl. b with 0


    ex1:
    00003FFF -> '00000000000000000b11111111111111' -> '000 0000' '000 0001' '111 1111 '111 1111'
                                    <--- 14 1 --->        len 7     len 7       len 7     len 7
    -> (drop all zeros, set bit 7th of each chunk but last to 1):
    '1|1111111 '0|1111111' -> hexa -> 0x_FF_7F

    ex2:
    00002000 -> '00000000000000000b10000000000000' -> +0000+  '000 0000' 000 0001' '100 0000' '000 0000'

    '1|100 0000' '0|000 0000' -> hexa -> 0x_C0_00

    ex3:
    00100000 -> '0000000000b100000000000000000000' -> +0000+ '000 0001' '100 0000' '000 0000' '000 0000'
    '1|1000000' '1|0000000' '0|0000000' -> hexa -> 0x_CO_80_00

    ex4:
    08000000 -> '000b1000000000000000000000000000' -> +000b+ '100 0000' '000 0000' '000 0000' '000 0000'
    '1|1000000' '1|0000000' '1|0000000' '00000000' -> hexa -> 0x_C0_80_80_00

    ex5
    001FFFFF -> '0000000000b111111111111111111111' -> +0000+ '000000b' '1111111' '1111111' '1111111'
    '1|1111111' '1|1111111' '0|1111111' -> hexa -> 0xFF_FF_7F

    ex6 (max value)
    0FFFFFFF -> '000b1111111111111111111111111111' -> +000b+ '111 1111' '111 1111' '111 1111' '111 1111'
    '1|111 1111' '1|111 1111' '1|111 1111' '0|111 1111' -> hexa -> 0xFF_FF_FF_7F


    ex7
    0x00000080 -> '00000000000000000000000b10000000' -> +0000+ '000 0000' '000 0000' '000 00b1' '000 0000'
    '1|000 00b1' '0|000 0000' -> hexa -> 0x_83_00

    for 32 bits cuts at [0, 4[, [4, 11[, [11, 18[, [18, 25[, [25, 32[
    """
    all_chunks = []
    for num in map(lambda n: hex(n), numbers):
        b = bin(int(num, SCALE_INP)).zfill(NBITS).replace('b', '0')

        if len(b) > NBITS: b = b[2:len(b)]
        assert len(b) == NBITS, f"Expected b: {b} to be of len {NBITS} - got {len(b)}"

        chunks = unpack(b)
        chunks = skip_leading_zeros(chunks) if b[0:OFFSET] == '0000' else \
            ['000' + b[0:OFFSET]] + chunks
        #
        all_chunks.append(chunks)
    ##
    all_l = []
    for grp in all_chunks:
        ##
        ## set leading bit for all grp
        chunks = list(map(lambda ch: str('1') + ch,
                          grp[0:len(grp) - 1])) + [str('0') + grp[-1]]
        ##
        ## map to hex. value and their decimal equiv, value
        l = list(
            map(lambda ch: int(hex(int(ch, SCALE_BIN)), SCALE_INP),
                chunks)
        )
        all_l = [*all_l, *l]
    ##
    return all_l


def decode(bytes_):
    pass


#
# Helpers
#

def unpack(b: str) -> List[str]:
    l = OFFSET
    chunks = []
    for h in range(OFFSET + ENC_LEN, NBITS + 1, ENC_LEN):
        chunks.append(b[l:h])         # [4, 11[, [11, 18[, [18, 25[, [25, 32[
        l = h
    ##
    return chunks

def skip_leading_zeros(chunks: List[str]) -> List[str]:
    jx, skip = 0, False
    for ix, ch in enumerate(chunks[0:OFFSET - 1]):  ## 3 first chunks only
        if ch == '0000000':                         ## only eliminate leftmost
            skip = True
            jx = ix
            continue
        break
        #
    if skip: jx += 1
    return chunks[jx:NBITS // (ENC_LEN + 1)]

#
# ini_string = "0x08000000"  => '0x08000000'
# b = bin(int(ini_string, scale)).zfill(32)
# b == '000b1000000000000000000000000000'
#
