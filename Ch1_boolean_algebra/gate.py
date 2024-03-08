# Implementation of nand, not, and, or, xor gate
# Only nand gate was implemented in python
# and the other gates was implemented only with the nand gate(or gates already implemented with this)
def nand_gate(a, b):
    if a == 1 and b == 1:
        return 0
    else:
        return 1


def not_gate(a):
    return nand_gate(a, a)


def and_gate(a, b):
    return not_gate(nand_gate(a, b))


def or_gate(a, b):
    return nand_gate(not_gate(a), not_gate(b))


def xor_gate(a, b):
    return and_gate(or_gate(a, b), nand_gate(a, b))
