from Ch1_boolean_algebra import gate


# Chip name: DFF
# input: d, output: q, function: q(t+1) = d(t)
class dff:
    def __init__(self):
        self.q = 0
        self.q_bar = 1

    def circuit(self, d, clk):
        self.q = gate.nand_gate(self.q_bar, gate.nand_gate(clk, d))
        self.q_bar = gate.nand_gate(self.q, gate.nand_gate(clk, gate.not_gate(d)))
        return self.q
