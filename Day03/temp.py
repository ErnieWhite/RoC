with open('input.txt', 'r', encoding='utf-8') as file:
    lines = file.read().splitlines()

count = 0
for line in lines:
    s = sorted([int(s) for s in line.split()]) 
    if (s[0] + s[1]) > s[2]:
        count += 1 


print(count)

