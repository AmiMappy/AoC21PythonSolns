inp_file = open("./21-Day2-input.txt", "r")
horiz = 0
depth = 0
aim = 0
for line in inp_file.readlines():
    line = line.split()
    if line[0] == "down":
        aim += int(line[1])
    elif line[0] == "up":
        aim -= int(line[1])
    elif line[0] == "forward":
        horiz += int(line[1])
        depth += aim * int(line[1])
print(horiz * depth)
        
