import ram

print('-------------ram8--------------')
x = [0, 0, 0, 0, 0, 0, 0, 0,
     0, 1, 0, 1, 0, 1, 1, 1]

y = [0, 0, 0, 0, 0, 0, 0, 0,
     1, 0, 0, 1, 0, 0, 0, 0]

zeros = [0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0]
inputs = [x, y, zeros, zeros, y, zeros]
loads = [1, 1, 0, 0, 0, 1]
addresses = [[0, 0, 0], [0, 1, 1], [0, 0, 1], [0, 1, 1], [0, 0, 0], [0, 0, 0]]
ram1 = ram.ram8()
time = -1
for i in range(12):
    clk = i % 2
    ram1.circuit(inputs[time], loads[time], addresses[time], clk)
    if clk == 0:
        time += 1
        print(ram1.out)
        print()
print()

print('-------------ram64--------------')
address = [0, 1, 2, 3, 4, 5]
print(address[:3])
print(address[3:])
