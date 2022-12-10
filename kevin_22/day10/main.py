import sys
print(sys.argv[1])
if sys.argv[1] == 'test':
    data_file = 'test_data.txt'
else:
    data_file   = 'data.txt'

power_map = {}

crt_output = [['.' for i in range(40)] for i in range(6)]
with open(data_file, 'r') as f:
    cycles = 0
    register_value = 1
    for line in f.readlines():
        cycle_count = 0
        if 'noop' in line:
            cycle_count = 1
        if 'addx' in line:
            cycle_count = 2
        for i in range(cycle_count):
            print(f'Cycles: {cycles} X-Register: {register_value} Row: {int(cycles/40)} Column: {(cycles % 40)} Sprite Range: {register_value-1}-{register_value+1}')
            if cycles % 40 >= register_value-1 and cycles % 40 <= register_value+1:
                crt_output[int(cycles/40)][cycles % 40] = '#'
            power_map[cycles] = cycles*register_value
            cycles += 1
        if 'addx' in line:
            register_value += int(line.split()[1])
            

print(f'Cycles: {cycles} X-Register: {register_value}')
power_map[cycles] = cycles*register_value
print(power_map[20]+power_map[60]+power_map[100]+power_map[140]+power_map[180]+power_map[220])
for line in crt_output:
    print(' '.join(line))