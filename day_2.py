with open("input_day_2.txt") as f:
    # Part 1
    # score = 0
    # for line in f:
    #     if line[2] == 'X':
    #         score += 1
    #         if line[0] == 'A':
    #             score += 3
    #         elif line[0] == 'C':
    #             score += 6
    #     elif line[2] == 'Y':
    #         score += 2
    #         if line[0] == 'B':
    #             score += 3
    #         elif line[0] == 'A':
    #             score += 6
    #     else:
    #         score += 3
    #         if line[0] == 'C':
    #             score += 3
    #         elif line[0] == 'B':
    #             score += 6
    # print(score)

    # Part 2
    score = 0
    for line in f:
        if line[2] == 'X':
            if line[0] == 'A':
                score += 3
            elif line[0] == 'B':
                score += 1
            else:
                score += 2
        elif line[2] == 'Y':
            score += 3
            if line[0] == 'A':
                score += 1
            elif line[0] == 'B':
                score += 2
            else:
                score += 3
        else:
            score += 6
            if line[0] == 'A':
                score += 2
            elif line[0] == 'B':
                score += 3
            else:
                score += 1
    print(score)