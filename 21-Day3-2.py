inp_file = open("./21-Day3-input.txt", "r")
bins = [x.strip('\n') for x in inp_file.readlines()]
carbs = bins
oxy = bins    
for i in range(len(bins[0])):
    c1 = 0
    c0 = 0
    for c in carbs:
        if c[i] == '0':
            c0 += 1
        else:
            c1 += 1
    if c1 == 0 or c0 == 0:
        break
    if c1 >= c0:
        carbs = list(filter(lambda x: x[i] == '0', carbs))
    else:
        carbs = list(filter(lambda x: x[i] == '1', carbs))
while len(oxy) != 1:    
    for i in range(len(bins[0])):
        c1 = 0
        c0 = 0
        for o in oxy:
            if o[i] == '1':
                c1 += 1
            else:
                c0 += 1
        if c1 >= c0:
            oxy = list(filter(lambda x: x[i] == '1', oxy))
        else:
            oxy = list(filter(lambda x: x[i] == '0', oxy))
print(int(oxy[0], base=2) * int(carbs[0], base=2))
