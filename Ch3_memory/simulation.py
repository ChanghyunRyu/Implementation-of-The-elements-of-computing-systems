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

print('-------------register---------------')
rgs1 = sequential_chip.register()
inputs = [1, 0, 0, 0, 0, 0]
loads = [1, 0, 0, 1, 0, 0]
time = -1
for i in range(12):
    clk = i % 2
    rgs1.circuit(inputs[time], loads[time], clk)
    if clk == 0:
        time += 1
        print('time = {}, load = {}, input = {}, out = {}'.format(time+1, loads[time], inputs[time], rgs1.out))
