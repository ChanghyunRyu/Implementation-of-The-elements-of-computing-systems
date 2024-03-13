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

print(multiplexer.demux_2bit(0, 0))
print(multiplexer.demux_2bit(1, 0))
print(multiplexer.demux_2bit(0, 1))
print(multiplexer.demux_2bit(1, 1))
print()
