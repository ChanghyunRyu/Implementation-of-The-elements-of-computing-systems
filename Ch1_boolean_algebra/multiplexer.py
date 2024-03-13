import gate


def mux_2bit(a, b, sel):
    return gate.or_gate(gate.and_gate(gate.not_gate(sel), a), gate.and_gate(sel, b))


def dmux_2bit(a, sel):
    return [gate.and_gate(a, gate.not_gate(sel)), gate.and_gate(a, sel)]


def mux_multi_bit(a, b, sel):
    temp = []
    for i in range(len(a)):
        temp.append(mux_2bit(a[i], b[i], sel))
    return temp


def mux_4_way_16(a, b, c, d, sel):
    result = []
    for i in range(len(a)):
        temp = [gate.mul_input_and_gate([a[i], gate.not_gate(sel[0]), gate.not_gate(sel[1])]),
                gate.mul_input_and_gate([b[i], gate.not_gate(sel[0]), sel[1]]),
                gate.mul_input_and_gate([c[i], sel[0], gate.not_gate(sel[1])]),
                gate.mul_input_and_gate([d[i], sel[0], sel[1]])]
        result.append(gate.mul_input_or_gate(temp))
    return result


def mux_8_way_16(a, b, c, d, e, f, g, h, sel):
    result = []
    for i in range(len(a)):
        temp = [gate.mul_input_and_gate([a[i], gate.not_gate(sel[0]), gate.not_gate(sel[1]), gate.not_gate(sel[2])]),
                gate.mul_input_and_gate([b[i], gate.not_gate(sel[0]), gate.not_gate(sel[1]), sel[2]]),
                gate.mul_input_and_gate([c[i], gate.not_gate(sel[0]), sel[1], gate.not_gate(sel[2])]),
                gate.mul_input_and_gate([d[i], gate.not_gate(sel[0]), sel[1], sel[2]]),
                gate.mul_input_and_gate([e[i], sel[0], gate.not_gate(sel[1]), gate.not_gate(sel[2])]),
                gate.mul_input_and_gate([f[i], sel[0], gate.not_gate(sel[1]), sel[2]]),
                gate.mul_input_and_gate([g[i], sel[0], sel[1], gate.not_gate(sel[2])]),
                gate.mul_input_and_gate([h[i], sel[0], sel[1], sel[2]])
                ]
        result.append(gate.mul_input_or_gate(temp))
    return result


def dmux_4_way(a, sel):
    return [gate.mul_input_and_gate([a, gate.not_gate(sel[0]), gate.not_gate(sel[1])]),
            gate.mul_input_and_gate([a, gate.not_gate(sel[0]), sel[1]]),
            gate.mul_input_and_gate([a, sel[0], gate.not_gate(sel[1])]),
            gate.mul_input_and_gate([a, sel[0], sel[1]])]


def dmux_8_way(a, sel):
    return [gate.mul_input_and_gate([a, gate.not_gate(sel[0]), gate.not_gate(sel[1]), gate.not_gate(sel[2])]),
            gate.mul_input_and_gate([a, gate.not_gate(sel[0]), gate.not_gate(sel[1]), sel[2]]),
            gate.mul_input_and_gate([a, gate.not_gate(sel[0]), sel[1], gate.not_gate(sel[2])]),
            gate.mul_input_and_gate([a, gate.not_gate(sel[0]), sel[1], sel[2]]),
            gate.mul_input_and_gate([a, sel[0], gate.not_gate(sel[1]), gate.not_gate(sel[2])]),
            gate.mul_input_and_gate([a, sel[0], gate.not_gate(sel[1]), sel[2]]),
            gate.mul_input_and_gate([a, sel[0], sel[1], gate.not_gate(sel[2])]),
            gate.mul_input_and_gate([a, sel[0], sel[1], sel[2]])
            ]
