# This ALU is designed in accordance with the computer 'hack' introduced in the book.
# Therefore, it implements only 18 functions rather than the 64 functions supported by the actual ALU.
# Additionally, this adder doesn't assume overflow.

# If the chips implemented in each chapter are not used in the next chapter, this is due to speed issue!!
from Ch1_boolean_algebra import gate
from Ch1_boolean_algebra import multiplexer


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


def incrementer(a):
    one = [0]*len(a)
    one[len(one)-1] = 1
    return adder(a, one)


def alu(x, y, zx, nx, zy, ny, f, no):
    # zx, nx
    zxs = [gate.not_gate(zx)]*len(x)
    x = gate.mul_and_gate(zxs, x)
    x = multiplexer.mux_multi_bit(x, gate.mul_not_gate(x), nx)

    # zy, ny
    zys = [gate.not_gate(zy)]*len(x)
    y = gate.mul_and_gate(zys, y)
    y = multiplexer.mux_multi_bit(y, gate.mul_not_gate(y), ny)

    # f
    tmp1 = adder(x, y)
    tmp2 = gate.mul_and_gate(x, y)
    out = multiplexer.mux_multi_bit(tmp2, tmp1, f)
    out = multiplexer.mux_multi_bit(out, gate.mul_not_gate(out), no)

    # zr, ng
    zr = gate.not_gate(gate.mul_input_or_gate(out))
    ng = out[0]
    return out, zr, ng
