# Advent of Code - 2016
# -- Day 7: Internet Protocol Version 7 ---


def get_input(f, encoding='utf-8'):
    with open(f,'r', encoding=encoding) as file:
        data = file.read().splitlines()
    return data


def split_address(address):
    hypernet = False
    b = [[],[]]
    d = []
    
    for c in address:
        if c in '[]':
            b[hypernet * --1].append(d)
            hypernet = not hypernet
            d = []
            continue
        d.append(c)
    if d:
        b[0].append(d)
    return b


def has_abba(lst):
    return any([any([c[i:i+2] == (c[i+2:i+4])[::-1] and c[i+1] != ((c[i+2:i+4])[::-1])[0] for i in range(len(c) - 3)]) for c in lst])


def is_tls(ip_address):
    supernet, hypernet = split_address(ip_address)
    return has_abba(supernet) and not has_abba(hypernet)


def get_abas(s):
    return  [''.join(x[i:i+3]) for x in s for i in range(len(x)-2) if x[i] == x[i+2] and x[i] != x[i+1]]

def get_babs(h, aba):
    return [''.join(x[i:i+3]) for a in aba for x in h for i in range(len(x)-2) if x[i] == x[i+2] and x[i] != x[i+1] and ''.join([x[i+1], x[i], x[i+1]]) == a ]


def is_ssl(ip_address):
    supernet, hypernet = split_address(ip_address)
    abas = get_abas(supernet)
    babs = get_babs(hypernet, abas)

    return len(babs) != 0 


def solver1(data):
    print(sum(is_tls(a) for a in data))


def solver2(data):
    b = [is_ssl(a) for a in data]
    print(sum(is_ssl(a) for a in data))


def main():
    data = get_input('input.txt')
    solver1(data)
    solver2(data)


if __name__ == '__main__':
    main()

