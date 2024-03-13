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


# Mul function is function that take multibits as input,calculate each operation, and then output multibits
def mul_not_gate(bits):
    temp = []
    for bit in bits:
        temp.append(not_gate(bit))
    return temp


def mul_and_gate(bits_a, bits_b):
    temp = []
    for i in range(len(bits_a)):
        temp.append(and_gate(bits_a[i], bits_b[i]))
    return


def mul_or_gate(bits_a, bits_b):
    temp = []
    for i in range(len(bits_a)):
        temp.append(or_gate(bits_a[i], bits_b[i]))
    return temp


def mul_input_and_gate(bits_a):
    result = 1
    for a in bits_a:
        result = and_gate(result, a)
    return result


def mul_input_or_gate(bits_a):
    result = 0
    for a in bits_a:
        result = or_gate(result, a)
    return result
