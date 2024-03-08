import gate


def mux_2bit(a, b, sel):
    return gate.or_gate(gate.and_gate(gate.not_gate(sel), a), gate.and_gate(sel, b))
