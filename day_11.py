import math

monkey_0 = [54, 82, 90, 88, 86, 54]
monkey_1 = [91, 65]
monkey_2 = [62, 54, 57, 92, 83, 63, 63]
monkey_3 = [67, 72, 68]
monkey_4 = [68, 89, 90, 86, 84, 57, 72, 84]
monkey_5 = [79, 83, 64, 58]
monkey_6 = [96, 72, 89, 70, 88]
monkey_7 = [79]
monkeys = [monkey_0, monkey_1, monkey_2, monkey_3, monkey_4, monkey_5, monkey_6, monkey_7]
cnt = [0] * 8
mod = 19 * 13 * 3 * 17 * 2 * 7 * 5 * 11

# hard code less and change round1/round2 boolean

for i in range(10000):
    print(i)
    for j in range(len(monkeys)):
        length = len(monkeys[j])
        cnt[j] += length
        for k in range(length):
            elem = monkeys[j].pop(0)
            if j == 0:
                new = elem * 7
                new = new % mod
                if new % 11 == 0:
                    monkeys[2].append(new)
                else:
                    monkeys[6].append(new)
            elif j == 1:
                new = elem * 13
                new = new % mod
                if new % 5 == 0:
                    monkeys[7].append(new)
                else:
                    monkeys[4].append(new)
            elif j == 2:
                new = elem + 1
                new = new % mod
                if new % 7 == 0:
                    monkeys[1].append(new)
                else:
                    monkeys[7].append(new)
            elif j == 3:
                new = elem * elem
                new = new % mod
                if new % 2 == 0:
                    monkeys[0].append(new)
                else:
                    monkeys[6].append(new)
            elif j == 4:
                new = elem + 7
                new = new % mod
                if new % 17 == 0:
                    monkeys[3].append(new)
                else:
                    monkeys[5].append(new)
            elif j == 5:
                new = elem + 6
                new = new % mod
                if new % 13 == 0:
                    monkeys[3].append(new)
                else:
                    monkeys[0].append(new)
            elif j == 6:
                new = elem + 4
                new = new % mod
                if new % 3 == 0:
                    monkeys[1].append(new)
                else:
                    monkeys[2].append(new)
            elif j == 7:
                new = elem + 8
                new = new % mod
                if new % 19 == 0:
                    monkeys[4].append(new)
                else:
                    monkeys[5].append(new)
items = sorted(cnt, reverse=True)
print(items[0] * items[1])