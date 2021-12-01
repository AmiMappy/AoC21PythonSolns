inp_file = open("./21-Day1-input.txt", "r")
n = [int(x) for x in inp_file.readlines()]
ans = 0
for x in range(len(n) - 1):    
    if n[x] < n[x + 1]:
        ans += 1
print(ans)
