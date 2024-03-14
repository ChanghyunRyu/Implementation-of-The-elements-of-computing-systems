import adder_unit
from Ch1_boolean_algebra import gate

x = [0, 0, 0, 0, 0, 0, 0, 0,
     0, 1, 0, 1, 0, 1, 1, 1]
y = [0, 0, 0, 0, 0, 0, 0, 0,
     1, 0, 0, 1, 0, 0, 0, 0]

# expect result: out = 0
print(adder_unit.alu(x, y, 1, 0, 1, 0, 1, 0))
print()

# expect result: out = 1
print(adder_unit.alu(x, y, 1, 1, 1, 1, 1, 1))
print()

# expect result: out = -1
print(adder_unit.alu(x, y, 1, 1, 1, 0, 1, 0))
print()

# expect result: out = x
print(adder_unit.alu(x, y, 0, 0, 1, 1, 0, 0))
print()

# expect result: out = y
print(adder_unit.alu(x, y, 1, 1, 0, 0, 0, 0))
print()

# expect result: !x
print(adder_unit.alu(x, y, 0, 0, 1, 1, 0, 1))
print()

# expect result: !y
print(adder_unit.alu(x, y, 1, 1, 0, 0, 0, 1))
print()

# expect result: -x
print(adder_unit.alu(x, y, 0, 0, 1, 1, 1, 1))
print()

# expect result: -y
print(adder_unit.alu(x, y, 1, 1, 0, 0, 1, 1))
print()

# expect result: x+1
print(adder_unit.alu(x, y, 0, 1, 1, 1, 1, 1))
print()

# expect result: y+1
print(adder_unit.alu(x, y, 1, 1, 0, 1, 1, 1))
print()

# expect result: x-1
print(adder_unit.alu(x, y, 0, 0, 1, 1, 1, 0))
print()

# expect result: y-1
print(adder_unit.alu(x, y, 1, 1, 0, 0, 1, 0))
print()

# expect result: x+y
print(adder_unit.alu(x, y, 0, 0, 0, 0, 1, 0))
print()

# expect result: x-y
print(adder_unit.alu(x, y, 0, 1, 0, 0, 1, 1))
print()

# expect result: y-x
print(adder_unit.alu(x, y, 0, 0, 0, 1, 1, 1))
print()

# expect result: x&y
print(adder_unit.alu(x, y, 0, 0, 0, 0, 0, 0))
print()

# expect result: x|y
print(adder_unit.alu(x, y, 0, 1, 0, 1, 0, 1))
print()
