with open("input_day_1.txt") as f:
    # Part 1
    arr = []
    cal = 0
    for line in f:
        if line == '\n':
            arr.append(cal)
            cal = 0
        else:
            cal += int(line)
    print(max(arr))

    # Part 2
    arr.sort(reverse=True)
    print(sum(arr[:3]))
