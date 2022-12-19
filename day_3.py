import string

alpha = dict(zip(string.ascii_lowercase, range(1, 27)))
alpha.update(dict(zip(string.ascii_uppercase, range(27, 53))))

with open("input_day_3.txt") as f:
    # pri = 0
    # for line in f:
    #     ruck_1 = line[:len(line)//2]
    #     ruck_2 = line[len(line)//2:]
    #     letter = ''.join(set(ruck_1).intersection(ruck_2))
    #     pri += alpha[letter]
    # print(pri)

    pri = 0
    idx = 0
    ruck = []
    for line in f:
        if (idx + 1) % 3 == 0:
            ruck.append(line)
            letter = ''.join(set(ruck[0]).intersection(set(ruck[1]), set(ruck[2])))
            ruck = []
            letter = letter.replace('\n', '')
            pri += alpha[letter]
        else:
            ruck.append(line)
        idx += 1
    print(pri)