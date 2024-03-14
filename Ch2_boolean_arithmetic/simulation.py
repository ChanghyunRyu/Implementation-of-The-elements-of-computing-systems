import adder_unit

print(adder_unit.half_adder(0, 0))
print(adder_unit.half_adder(0, 1))
print(adder_unit.half_adder(1, 0))
print(adder_unit.half_adder(1, 1))
print()

print(adder_unit.full_adder(0, 0, 0))
print(adder_unit.full_adder(0, 0, 1))
print(adder_unit.full_adder(0, 1, 0))
print(adder_unit.full_adder(0, 1, 1))
print(adder_unit.full_adder(1, 0, 0))
print(adder_unit.full_adder(1, 0, 1))
print(adder_unit.full_adder(1, 1, 0))
print(adder_unit.full_adder(1, 1, 1))
print()

a = [1, 0, 1, 1]
b = [0, 0, 1, 0]
print(adder_unit.adder(a, b))
print()

print(adder_unit.incrementer(a))
print()
