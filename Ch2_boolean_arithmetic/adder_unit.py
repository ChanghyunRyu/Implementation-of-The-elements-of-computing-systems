# This ALU is designed in accordance with the computer 'hack' introduced in the book.
# Therefore, it implements only 18 functions rather than the 64 functions supported by the actual ALU.
# Additionally, this adder doesn't assume overflow.
from Ch1_boolean_algebra import gate


def half_adder(a, b):
    return gate.and_gate(a, b), gate.xor_gate(a, b)


def full_adder(a, b, c):
    c1, s1 = half_adder(a, b)
    c2, s2 = half_adder(s1, c)
    return gate.or_gate(c1, c2), s2


def adder(a, b):
    result = [0]*len(a)
    carry = 0
    for i in range(len(a)):
        carry, s = full_adder(a[len(a)-1-i], b[len(a)-1-i], carry)
        result[len(a)-1-i] = s
    return result
