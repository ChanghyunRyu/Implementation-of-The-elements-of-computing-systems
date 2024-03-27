# RAM8, RAM64, RAM512, RAM4K, RAM16K 순으로 구현.
from Ch1_boolean_algebra import gate
from Ch1_boolean_algebra import multiplexer
import sequential_chip


# Chip name: RAM^n
# input: in[16], load, address[k](k = log2(n))
# output: out[16]
class ram8:
    def __init__(self):
        self.out = [0]*16
        self.regs = []
        for _ in range(8):
            self.regs.append(sequential_chip.register_16bit())

    def circuit(self, d_16bit, load, address, clk):
        loads = multiplexer.dmux_8_way(load, address)
        for i in range(8):
            self.regs[i].circuit(d_16bit, loads[i], clk)
        self.out = multiplexer.mux_8_way_16(self.regs[0].out, self.regs[1].out, self.regs[2].out, self.regs[3].out,
                                            self.regs[4].out, self.regs[5].out, self.regs[6].out, self.regs[7].out,
                                            address)
        return self.out


class ram64:
    def __init__(self):
        self.out = [0]*16
        self.ram8s = []
        for _ in range(8):
            self.ram8s.append(ram8())

    def circuit(self, d_16bit, load, address, clk):
        ram_address = address[:3]
        reg_address = address[3:]
        loads = multiplexer.dmux_8_way(load, ram_address)
        for i in range(8):
            self.ram8s[i].circuit(d_16bit, loads[i], reg_address, clk)
        self.out = multiplexer.mux_8_way_16(self.ram8s[0].out, self.ram8s[1].out, self.ram8s[2].out, self.ram8s[3].out,
                                            self.ram8s[4].out, self.ram8s[5].out, self.ram8s[6].out, self.ram8s[7].out,
                                            ram_address)
        return self.out
