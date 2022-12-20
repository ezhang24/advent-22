txt = open("input_day_6.txt").read().splitlines()
str = txt[0]

# Part 1
for idx in range(0, len(str)-3):
    marker = str[idx:idx+4]
    letter = [x for x in marker]
    if len(set(letter)) == 4:
        print(idx+4)
        break

# Part 2
for idx in range(0, len(str)-13):
    marker = str[idx:idx+14]
    letter = [x for x in marker]
    if len(set(letter)) == 14:
        print(idx+14)
        break