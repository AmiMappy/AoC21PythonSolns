inp_file = open("./21-Day3-input.txt", "r")
bins = [x.strip('\n') for x in inp_file.readlines()]
l = len(bins[0])
gamma = ""
epsilon = ""
for i in range(l):
    count1 = count0 = 0
    for x in bins:        
        if x[i] == '1':
            count1 += 1            
        else:
            count0 += 1    
    if count1 > count0:
        gamma += '1'
        epsilon += '0'
    else:
        gamma += '0'
        epsilon += '1'
print(int(gamma,base=2) * int(gamma,base=2))
