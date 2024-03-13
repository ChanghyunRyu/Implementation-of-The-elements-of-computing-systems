import gate
import multiplexer

print(gate.not_gate(0))
print(gate.not_gate(1))
print()

print(gate.and_gate(0, 0))
print(gate.and_gate(0, 1))
print(gate.and_gate(1, 0))
print(gate.and_gate(1, 1))
print()

print(gate.or_gate(0, 0))
print(gate.or_gate(0, 1))
print(gate.or_gate(1, 0))
print(gate.or_gate(1, 1))
print()

print(gate.xor_gate(0, 0))
print(gate.xor_gate(0, 1))
print(gate.xor_gate(1, 0))
print(gate.xor_gate(1, 1))
print()

print(multiplexer.mux_2bit(1, 0, 0))
print(multiplexer.mux_2bit(1, 0, 1))
print()

print(multiplexer.dmux_2bit(0, 0))
print(multiplexer.dmux_2bit(1, 0))
print(multiplexer.dmux_2bit(0, 1))
print(multiplexer.dmux_2bit(1, 1))
print()

a = [1, 0, 0, 0, 1, 1, 0, 1]
b = [0, 1, 1, 1, 0, 1, 0, 0]
print(multiplexer.mux_multi_bit(a, b, 0))
print(multiplexer.mux_multi_bit(a, b, 1))
print()

temp1 = [1, 0, 0]
temp2 = [1, 1, 1]
temp3 = [0, 0, 0]
print(gate.mul_input_and_gate(temp1))
print(gate.mul_input_and_gate(temp2))
print(gate.mul_input_and_gate(temp3))
print(gate.mul_input_or_gate(temp1))
print(gate.mul_input_or_gate(temp2))
print(gate.mul_input_or_gate(temp3))
print()

c = [0, 0, 0, 0, 0, 0, 1, 1]
d = [1, 1, 1, 1, 1, 1, 1, 1]
print(multiplexer.mux_4_way_16(a, b, c, d, [0, 0]))
print(multiplexer.mux_4_way_16(a, b, c, d, [0, 1]))
print(multiplexer.mux_4_way_16(a, b, c, d, [1, 0]))
print(multiplexer.mux_4_way_16(a, b, c, d, [1, 1]))
print()

e = [0, 1, 1, 1, 1, 1, 1, 1]
f = [0, 0, 0, 0, 0, 1, 1, 1]
g = [0, 0, 0, 0, 1, 1, 1, 1]
h = [0, 0, 0, 1, 1, 1, 1, 1]
print(multiplexer.mux_8_way_16(a, b, c, d, e, f, g, h, [0, 0, 0]))
print(multiplexer.mux_8_way_16(a, b, c, d, e, f, g, h, [0, 0, 1]))
print(multiplexer.mux_8_way_16(a, b, c, d, e, f, g, h, [0, 1, 0]))
print(multiplexer.mux_8_way_16(a, b, c, d, e, f, g, h, [0, 1, 1]))
print(multiplexer.mux_8_way_16(a, b, c, d, e, f, g, h, [1, 0, 0]))
print(multiplexer.mux_8_way_16(a, b, c, d, e, f, g, h, [1, 0, 1]))
print(multiplexer.mux_8_way_16(a, b, c, d, e, f, g, h, [1, 1, 0]))
print(multiplexer.mux_8_way_16(a, b, c, d, e, f, g, h, [1, 1, 1]))
print()

print(multiplexer.dmux_4_way(1, [0, 0]))
print(multiplexer.dmux_4_way(1, [0, 1]))
print(multiplexer.dmux_4_way(1, [1, 0]))
print(multiplexer.dmux_4_way(1, [1, 1]))
print()
