inp_file = open("./testinp5.txt", "r")
lines = [x.strip('\n') for x in inp_file.readlines()]

coords = {} # key = left coord : value = right coords
maxx = maxy = 0

for coord in lines:
    l = coord.partition(' -> ')    
    maxx = max(maxx, int(l[0].split(',')[0]))
    maxy = max(maxy, int(l[0].split(',')[1]))
    maxx = max(maxx, int(l[2].split(',')[0]))
    maxy = max(maxy, int(l[2].split(',')[1]))    
    if l[0] in coords:
        coords[l[0]].append(l[2])
    else:
        coords[l[0]] = [l[2]]

mp = []
for i in range(maxx + 1):
    mps = []
    for j in range(maxy + 1):
        mps.append(0)
    mp.append(mps)

for lc in coords:
    for a in coords[lc]:
        if lc.split(',')[0] == a.split(',')[0]: # X-coordinate remains constant       
            x = int(lc.split(',')[0])
            y1 = int(lc.split(',')[1])
            y2 = int(a.split(',')[1])
            for y in range(min(y1, y2), max(y1, y2) + 1):
                mp[y][x] += 1                
        elif lc.split(',')[1] == a.split(',')[1]: # Y-coordinate remains constant                
            y = int(lc.split(',')[1])
            x1 = int(lc.split(',')[0])
            x2 = int(a.split(',')[0])
            for x in range(min(x1, x2), max(x1, x2) + 1):
                mp[y][x] += 1
        else:
            x1 = int(lc.split(',')[0])
            x2 = int(a.split(',')[0])
            y1 = int(lc.split(',')[1])
            y2 = int(a.split(',')[1])
            dirx = diry = 0
            if x1 > x2:
                dirx = -1
            else:
                dirx = 1
            if y1 > y2:
                diry = -1
            else:
                diry = 1
            while x1 != x2 and y1 != y2:                
                mp[y1][x1] += 1
                x1 += dirx
                y1 += diry
            mp[y1][x1] += 1
ans = 0

for row in mp:
    for elem in row:
        if elem >= 2:
            ans += 1
for mps in mp:
    print(mps)
print(ans)
