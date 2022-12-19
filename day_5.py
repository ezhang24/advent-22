crates = [['B', 'P', 'N', 'Q', 'H', 'D', 'R', 'T'], ['W', 'G', 'B', 'J', 'T', 'V'],
['N', 'R', 'H', 'D', 'S', 'V', 'M', 'Q'], ['P', 'Z', 'N', 'M', 'C'], ['D', 'Z', 'B'],
['V', 'C', 'W', 'Z'], ['G', 'Z', 'N', 'C', 'V', 'Q', 'L', 'S'], ['L', 'G', 'J', 'M', 'D', 'N', 'V'],
['T', 'P', 'M', 'F', 'Z', 'C', 'G']]

txt = open("input_day_5.txt").read().splitlines()

# for rule in txt:
#     lst = [int(w) for w in rule.split() if w.isdigit()]
#     move_boxes = crates[lst[1]-1][-lst[0]:]
#     crates[lst[1]-1] = crates[lst[1]-1][:-lst[0]]
#     crates[lst[2]-1] = crates[lst[2]-1] + move_boxes[::-1]

# end = ""
# for crate in crates:
#     end += crate[-1]
# print(end)

for rule in txt:
    lst = [int(w) for w in rule.split() if w.isdigit()]
    move_boxes = crates[lst[1]-1][-lst[0]:]
    crates[lst[1]-1] = crates[lst[1]-1][:-lst[0]]
    crates[lst[2]-1] = crates[lst[2]-1] + move_boxes

end = ""
for crate in crates:
    end += crate[-1]
print(end)