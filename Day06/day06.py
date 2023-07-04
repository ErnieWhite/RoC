# --- Advent of Code 2016---
# --- Day 6: Signals and Noise ---

def get_data():

    with open('input.txt', 'r', encoding='utf-8') as file:
        data = file.readlines()

    return data

def solver(signals, which='m'):
    if which == 'm':  # return the most common characters
        position = -1
    elif which == 'l':  # return the least common characters
        position = 0

    sig_len = len(signals[0])
    counts = [{} for _ in range(sig_len)]

    for signal in signals:
        for i, c in enumerate(signal):
            counts[i][c] = counts[i][c] + 1 if c in counts[i] else 1
    communication = [] 
    for d in counts:
        p = list(d.items())
        p.sort(key=lambda x: x[1])
        communication.append(p[position][0])

    return ''.join(communication)


def main():
    data = get_data()
    print(f"Part 1: {solver(data, 'm')}")
    print(f"Part 2: {solver(data, 'l')}")


if __name__ == '__main__':
    main()

