inp_file = open("./21-Day1-input.txt", "r")
n = [int(x) for x in inp_file.readlines()]
ans = 0
prev = sum(n[:3])
for x in range(1, len(n) - 2):
    curr = sum(n[x:x+3])    
    if curr > prev:        
        ans += 1
    prev = curr                
print(ans)
