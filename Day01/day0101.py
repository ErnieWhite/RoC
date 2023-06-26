# --- Day 1: No Time for a Taxicab ---
# adventofcode.com/2016/day/1


def turn(d, f):
    turns = {
            'N': {'L': 'W', 'R': 'E'},
            'S': {'L': 'E', 'R': 'W'},
            'E': {'L': 'N', 'R': 'S'},
            'W': {'L': 'S', 'R': 'N'},
            }
    return turns[f][d[0]]

def move(d, f):
    delta = {
            'N': {'L': (-1, 0), 'R': (1, 0)},
            'S': {'L': (1, 0), 'R': (-1, 0)},
            'E': {'L': (0, 1), 'R': (0, -1)},
            'W': {'L': (0, -1), 'R': (0, 1)},
            }
    direction = d[0]
    return delta[f][direction] 


def main():
    with open("input.txt", "r") as dataFile:
        data = dataFile.read()
    directions = data.split(', ')
    x = 0
    y = 0
    f = 'N'
    
    for direction in directions:
        delta = move(direction, f)
        f = turn(direction, f)

        distance = int(direction[1:])
        x -= distance * delta[0]
        y -= distance * delta[1]

    print (abs(x) + abs(y))


if __name__ == '__main__':
    main()
