import sequential_chip

print('-------------dff---------------')
dff1 = sequential_chip.dff()
inputs = [1, 0, 0, 1, 0, 1]
time = -1
for i in range(12):
    clk = i % 2
    dff1.circuit(inputs[time], clk)
    if clk == 0:
        time += 1
        print('time = {}, input = {}, q = {}'.format(time+1, inputs[time], dff1.q))
print()

print('-------------register_bit---------------')
rgs1 = sequential_chip.register_bit()
inputs = [1, 0, 0, 0, 0, 0]
loads = [1, 0, 0, 1, 0, 0]
time = -1
for i in range(12):
    clk = i % 2
    rgs1.circuit(inputs[time], loads[time], clk)
    if clk == 0:
        time += 1
        print('time = {}, load = {}, input = {}, out = {}'.format(time+1, loads[time], inputs[time], rgs1.out))

print('-------------register_16bit---------------')
x = [0, 0, 0, 0, 0, 0, 0, 0,
     0, 1, 0, 1, 0, 1, 1, 1]
y = [0, 0, 0, 0, 0, 0, 0, 0,
     1, 0, 0, 1, 0, 0, 0, 0]
zeros = [0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0]
rgs2 = sequential_chip.register_16bit()
inputs = [x, zeros, zeros, zeros, y, zeros]
loads = [1, 0, 0, 1, 1, 0]
time = -1
for i in range(12):
    clk = i % 2
    rgs2.circuit(inputs[time], loads[time], clk)
    if clk == 0:
        time += 1
        print('time = {}, load = {}, input = {}, out = {}'.format(time+1, loads[time], inputs[time], rgs2.out))
