from Ch1_boolean_algebra import gate
from Ch1_boolean_algebra import multiplexer
# Originally, data flip-flop and register don't have initial value.
# Since we did not assume the case of entering the 'None' value into the existing chip, initial value is set to 0.


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


# Chip name: register
# input: d, load , output: out,
# function: if load(t) then out(t+1) = d(t), else out(t+1) = out(t)
class register_bit:
    def __init__(self):
        self.out = 0
        self.dff = dff()

    def circuit(self, d, load, clk):
        self.out = self.dff.circuit(multiplexer.mux_2bit(self.out, d, load), clk)
        return self.out


# Chip name: register_16bit
# input: d[16], load , output: out[16]
# function: if load(t) then out(t+1) = d(t), else out(t+1) = out(t), "="은 16비트 연산.
class register_16bit:
    def __init__(self):
        self.out = [0]*16
        self.reg = []
        for _ in range(16):
            self.reg.append(register_bit())

    def circuit(self, d_16bit, load, clk):
        for i in range(16):
            self.out[i] = self.reg[i].circuit(d_16bit[i], load, clk)
        return self.out
