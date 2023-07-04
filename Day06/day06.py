# --- Advent of Code 2016---
# --- Day 6: Signals and Noise ---

from pprint import pprint

def get_data():
    data = [
            'eedadn', 'drvtee', 'eandsr', 'raavrd', 
            'atevrs', 'tsrnev', 'sdttsa', 'rasrtv',
            'nssdts', 'ntnada', 'svetve', 'tesnvt',
            'vntsnd', 'vrdear', 'dvrsen', 'enarar',
            ]

    return data

def solver01(signals):
    sig_len = len(signals[0])
    counts = [{} for _ in range(sig_len)]

    for signal in signals:
        for i, c in enumerate(signal):
            counts[i][c] = counts[i][c] + 1 if c in counts[i] else 1
    for d in counts:
        p = list(d.items())
        p.sort(key=lambda x: x[1])
        print(p[-1][0], end='') 
    print()


def main():
    data = get_data()
    solver01(data)


if __name__ == '__main__':
    main()

