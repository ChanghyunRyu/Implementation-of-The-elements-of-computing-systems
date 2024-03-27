import sequential_chip
from Ch2_boolean_arithmetic import adder_unit
from Ch1_boolean_algebra import multiplexer
from Ch1_boolean_algebra import gate


class counter:
    def __init__(self):
        self.reg = sequential_chip.register_16bit()
        self.out = [0]*16

    def circuit(self, d_16bit, load, inc, reset, clk):
        resets = [gate.not_gate(reset)]*16
        d_16bit = gate.mul_and_gate(d_16bit, resets)
        d_16bit = multiplexer.mux_multi_bit(d_16bit, adder_unit.incrementer(d_16bit), inc)
        load = gate.mul_input_or_gate([load, inc, reset])
        self.out = self.reg.circuit(d_16bit, load, clk)

        return self.out
