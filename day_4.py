with open("input_day_4.txt") as f:
    # cnt = 0
    # for line in f:
    #     lst = line.split(',')
    #     idx = lst[0].find('-')
    #     num_1 = int(lst[0][:idx])
    #     num_2 = int(lst[0][idx+1:])
    #     idx = lst[1].find('-')
    #     num_3 = int(lst[1][:idx])
    #     num_4 = int(lst[1][idx+1:-1])
    #     if all(item in list(range(num_3, num_4+1)) for item in list(range(num_1, num_2+1))) or all(item in list(range(num_1, num_2+1)) for item in list(range(num_3, num_4+1))):
    #         cnt += 1
    # print(cnt)

    cnt = 0
    for line in f:
        lst = line.split(',')
        idx = lst[0].find('-')
        num_1 = int(lst[0][:idx])
        num_2 = int(lst[0][idx+1:])
        idx = lst[1].find('-')
        num_3 = int(lst[1][:idx])
        num_4 = int(lst[1][idx+1:-1])
        if any(item in list(range(num_3, num_4+1)) for item in list(range(num_1, num_2+1))) or any(item in list(range(num_1, num_2+1)) for item in list(range(num_3, num_4+1))):
            cnt += 1
    print(cnt)
