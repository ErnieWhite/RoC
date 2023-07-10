# Advent of Code - 2016
# --- Day 8: Two-Factor Authentication ---

class Screen:
    def __init__(self, dimensions):
        self.c, self.rows = (int(x) for x in dimensions.split('x'))
        self.c = int(self.c)
        self.r = int(self.r)
        self.scr = [['.' for _ in range(self.c)] for _ in range(self.r)]

    def update(self, o):
        t = o.split()
        if t[0] == 'rect':
            self.rect(t[1])
        if t[0] == 'rotate' and t[1] == 'row':
            self.rotate_row(*t[2:])
        if t[0] == 'rotate' and t[1] == 'column':
            self.rotate_col(*t[2:])

    def display(self):
        for line in self.scr:
            print(''.join(line))

    def rect(self, size):
        cols, rows = tuple(int(x) for x in size.split('x'))
        for r in range(rows):
            for c in range(cols):
                self.scr[r][c] = '#'

    def rotate_row(self, *args):
        r = int(args[0].split('=')[1])
        n = int(args[2])
        if n > 0:
            for _ in range(n):
                t = self.scr[r].pop()
                self.scr[r].insert(0, t)
        else:
            for _ in range(abs(n)):
                t = self.scr[r].pop(0)
                self.scr[r].append(t)

    def rotate_col(self, *args):
        c = int(args[0].split('=')[1])
        n = int(args[2])
        if n > 0:
            for _ in range(n):
                t = self.scr[-1][c]
                for r in range(self.r-1, 0, -1):
                    self.scr[r][c] = self.scr[r-1][c]
                self.scr[0][c] = t
        else:
            for _ in range(abs(n)):
                t = self.scr[0][c]
                for r in range(0, self.r-1):
                    self.scr[r][c] = self.scr[r+1][c]
                self.scr[-1][c] = t

    def p_cnt(self):
        return sum([self.scr[r][c] == '#' for c in range(self.c) for r in range(self.r)])

def s(d):
    scr = Screen('50x6')
    for e in d:
        scr.update(e)
    scr.display()
    print(scr.p_cnt())

def main():
    with open('input.txt') as file:
        d = file.read().splitlines()
    s(d)

if __name__ == '__main__':
    main()
