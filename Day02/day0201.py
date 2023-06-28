with open("input.txt", "r", encoding="utf-8") as data:
    instructions = data.readlines()

r = 1
c = 1
p = ''
keypad = [ ['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9'] ]
delta = { 'U': (0, -1), 'D': (0, 1), 'L': (-1, 0), 'R': (1, 0), }

for instruction in instructions:
    for move in list(instruction.strip('\n')):
        c += delta[move][0]
        r += delta[move][1]

        if r < 0:
            r = 0
        if r >= len(keypad) - 1:
            r = len(keypad) - 1

        if c < 0:
            c = 0
        if c >= len(keypad[0]) - 1:
            c = len(keypad[0]) - 1
    p += keypad[r][c]

print(p)
