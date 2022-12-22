import numpy as np

txt = open("input_day_9.txt").read().splitlines()

def move_knot(front, back):
    diff_x = front[0] - back[0]
    diff_y = front[1] - back[1]
    if abs(diff_x) > 1 or abs(diff_y) > 1:
        back[0] = back[0] + np.sign(diff_x)
        back[1] = back[1] + np.sign(diff_y)
    return back

# CHANGE LIST TO TUPLE LATER
head = [0, 0]
tail = [0, 0]
moves = set()
for line in txt:
    move = line.split()
    for i in range(int(move[1])):
        if move[0] == 'R':
            head[0] += 1
        elif move[0] == 'L':
            head[0] -= 1
        elif move[0] == 'U':
            head[1] += 1
        else:
            head[1] -= 1
        tail = move_knot(head, tail)
        tail_move = [str(x) for x in tail]
        moves.add(','.join(tail_move))
print(len(moves))

# Part 2
head = [0, 0]
knot_1 = [0, 0]
knot_2 = [0, 0]
knot_3 = [0, 0]
knot_4 = [0, 0]
knot_5 = [0, 0]
knot_6 = [0, 0]
knot_7 = [0, 0]
knot_8 = [0, 0]
knot_9 = [0, 0]
moves = set()

for line in txt:
    move = line.split()
    for i in range(int(move[1])):
        if move[0] == 'R':
            head[0] += 1
        elif move[0] == 'L':
            head[0] -= 1
        elif move[0] == 'U':
            head[1] += 1
        else:
            head[1] -= 1
        knot_1 = move_knot(head, knot_1)
        knot_2 = move_knot(knot_1, knot_2)
        knot_3 = move_knot(knot_2, knot_3)
        knot_4 = move_knot(knot_3, knot_4)
        knot_5 = move_knot(knot_4, knot_5)
        knot_6 = move_knot(knot_5, knot_6)
        knot_7 = move_knot(knot_6, knot_7)
        knot_8 = move_knot(knot_7, knot_8)
        knot_9 = move_knot(knot_8, knot_9)

        knot_9_move = [str(x) for x in knot_9]
        moves.add(','.join(knot_9_move))

print(len(moves))


