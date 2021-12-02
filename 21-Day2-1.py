inp_file = open("./21-Day2-input.txt", "r")
horiz = 0
depth = 0
for line in inp_file.readlines():
    line = line.split()
    if line[0] == "forward":
        horiz += int(line[1])
    elif line[0] == "up":
        depth -= int(line[1])
    else:
        depth += int(line[1])
print(horiz * depth)
        
