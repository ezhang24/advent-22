txt = open("input_day_10.txt").read().splitlines()

num_cycles = 0
for line in txt:
    inst = line.split()
    if inst[0] == 'noop':
        num_cycles += 1
    else:
        num_cycles += 2

val = 1
signal_sum = 0
idx = 0
add = 0
cycle = 0
curr = txt[idx]
prev = -1
for i in range(num_cycles):
    inst = curr.split()
    if inst[0] == 'addx' and prev != idx:
        add = int(inst[1])
        cycle = i + 1
        prev = idx
    elif inst[0] == 'noop' and prev != idx:
        add = 0
        cycle = i
        prev = idx

    if (i%40) in range(val-1, val+2):
        print("#", end="")
    else:
        print(".", end="")

    if i+1 == 20:
        signal_sum += 20 * val
    elif i+1 == 60:
        signal_sum += 60 * val
    elif i+1 == 100:
        signal_sum += 100 * val
    elif i+1 == 140:
        signal_sum += 140 * val
    elif i+1 == 180:
        signal_sum += 180 * val
    elif i+1 == 220:
        signal_sum += 220 * val

    if (i+1) % 40 == 0:
        print()

    if i == cycle:
        val += add
        if idx+1 != len(txt):
            idx += 1
            curr = txt[idx]
print(signal_sum)