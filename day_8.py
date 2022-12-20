txt = open("input_day_8.txt").read().splitlines()

grid = []
for line in txt:
    grid.append([c for c in line])

def check_up(r, c):
    for i in range(0, r):
        if grid[i][c] >= grid[r][c]:
            return False
    return True

def check_down(r, c):
    for i in range(r+1, len(grid)):
        if grid[i][c] >= grid[r][c]:
            return False
    return True

def check_left(r, c):
    for i in range(0, c):
        if grid[r][i] >= grid[r][c]:
            return False
    return True

def check_right(r, c):
    for i in range(c+1, len(grid[0])):
        if grid[r][i] >= grid[r][c]:
            return False
    return True

def count_up(r, c):
    cnt = 0
    for i in range(r-1, -1, -1):
        if grid[i][c] >= grid[r][c]:
            cnt += 1
            return cnt
        else:
            cnt += 1
    return cnt

def count_down(r, c):
    cnt = 0
    for i in range(r+1, len(grid)):
        if grid[i][c] >= grid[r][c]:
            cnt += 1
            return cnt
        else:
            cnt += 1
    return cnt

def count_left(r, c):
    cnt = 0
    for i in range(c-1, -1, -1):
        if grid[r][i] >= grid[r][c]:
            cnt += 1
            return cnt
        else:
            cnt += 1
    return cnt

def count_right(r, c):
    cnt = 0
    for i in range(c+1, len(grid[0])):
        if grid[r][i] >= grid[r][c]:
            cnt += 1
            return cnt
        else:
            cnt += 1
    return cnt

# Part 1
visible = 0
for r in range(len(grid)):
    for c in range(len(grid[0])):
        if r - 1 < 0 or c - 1 < 0 or r + 1 >= len(grid) or c + 1 >= len(grid[0]):
            visible += 1
        else:
            if check_up(r, c) or check_down(r, c) or check_left(r, c) or check_right(r, c):
                visible += 1
print(visible)

# Part 2
best = -1
for r in range(len(grid)):
    for c in range(len(grid[0])):
        if r - 1 > 0 and c - 1 > 0 and r + 1 < len(grid)-1 and c + 1 < len(grid[0])-1:
            score = count_up(r, c) * count_down(r, c) * count_left(r, c) * count_right(r, c)
            if score > best:
                best = score
print(best)