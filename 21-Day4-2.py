inp_file = open("./21-Day4-input.txt", "r")
numbers = []
grids = [] # A 3D list

# preparing grids and numbers for action
num_flag = 0
grid_flag = 0
temp = []
lines = inp_file.readlines()
for line in lines:    
    if line != '\n':
        temp.append(line)
    else:
        if num_flag == 0:
            for l in temp:
                numbers.append(l.strip('\n'))
            num_flag = 1
        else:
            grid = []
            for l in temp:
                grid.append(l.strip('\n'))
            grids.append(grid)
        temp = []
grid = lines[-(len(grids[0]))::]
for i in range(len(grid)):
    grid[i] = grid[i].strip('\n')
grids.append(grid)

numbers = numbers[0].split(',')

for i in range(len(grids)):
    for j in range(len(grids[i])):
        grids[i][j] = grids[i][j].split()
        for k in range(len(grids[i][j])):
            grids[i][j][k] = int(grids[i][j][k])

# solution begins
def bingo_find(grids):
    bingo = 0
    bingo_grid = []
    n = -1
    for num in numbers:
        if bingo == 0:            
            num = int(num)
            for grid in grids:
                for row in grid:
                    if num in row:
                        row[row.index(num)] = -1                        
            for grid in grids:
                if bingo == 0:
                    # 1. Row is bingo
                    for row in grid:
                        if row == [-1] * len(grid):
                            bingo = 1
                            bingo_grid = grid
                            n = num
                            break
                    # 2. Column is bingo
                    if bingo == 0:
                        for i in range(len(grid)):
                            count = 0
                            for row in grid:
                                if row[i] == -1:
                                    count += 1
                            if count == len(grid):
                                bingo = 1
                                bingo_grid = grid
                                n = num
                                break
    return [bingo_grid, n]
while len(grids) > 1:
    grids.remove(bingo_find(grids)[0])
print(bingo_find(grids))
# look at output and calculate answer yourself
=======
inp_file = open("./21-Day4-input.txt", "r")
numbers = []
grids = [] # A 3D list

# preparing grids and numbers for action
num_flag = 0
grid_flag = 0
temp = []
lines = inp_file.readlines()
for line in lines:    
    if line != '\n':
        temp.append(line)
    else:
        if num_flag == 0:
            for l in temp:
                numbers.append(l.strip('\n'))
            num_flag = 1
        else:
            grid = []
            for l in temp:
                grid.append(l.strip('\n'))
            grids.append(grid)
        temp = []
grid = lines[-(len(grids[0]))::]
for i in range(len(grid)):
    grid[i] = grid[i].strip('\n')
grids.append(grid)

numbers = numbers[0].split(',')

for i in range(len(grids)):
    for j in range(len(grids[i])):
        grids[i][j] = grids[i][j].split()
        for k in range(len(grids[i][j])):
            grids[i][j][k] = int(grids[i][j][k])

# solution begins
def bingo_find(grids):
    bingo = 0
    bingo_grid = []
    n = -1
    for num in numbers:
        if bingo == 0:            
            num = int(num)
            for grid in grids:
                for row in grid:
                    if num in row:
                        row[row.index(num)] = -1                        
            for grid in grids:
                if bingo == 0:
                    # 1. Row is bingo
                    for row in grid:
                        if row == [-1] * len(grid):
                            bingo = 1
                            bingo_grid = grid
                            n = num
                            break
                    # 2. Column is bingo
                    if bingo == 0:
                        for i in range(len(grid)):
                            count = 0
                            for row in grid:
                                if row[i] == -1:
                                    count += 1
                            if count == len(grid):
                                bingo = 1
                                bingo_grid = grid
                                n = num
                                break
    return [bingo_grid, n]
while len(grids) > 1:
    grids.remove(bingo_find(grids)[0])
print(bingo_find(grids))
# look at output and calculate answer yourself
