# Advent of Code - 2016
# --- Day 4: Security Through Obscurity ---

from collections import Counter
import re


def get_data():
    with open('input.txt', 'r', encoding='utf-8') as file:
        rooms = file.read().split('\n')
    return rooms


def clean_data(data):

    cleaned_data = []

    for room in data:
        if room == '':
            continue

        name = [c for c in room.split('[')[0] if not c in '0123456789']
        cleaned_name = [c for c in name if not c == '-']

        sector_id = int(''.join([d for d in room if d in '0123456789']))
        checksum = ''.join(re.split('\[|\]', room)[1])
        counts = sorted(list(Counter(cleaned_name).items()), key=lambda x: (100-x[1], x[0]))
        top_five = ''.join([c[0] for c in counts[:5]])

        if top_five == (checksum):
            cleaned_data.append([name, sector_id])
    return cleaned_data 


def decipher_room_name(room):
    decript_dict = {'a':'b', 'b':'c', 'c':'d', 'd':'e', 'e':'f', 'f':'g', 'g':'h', 'h':'i', 'i':'j', 'j':'k', 'k':'l', 
                    'l':'m', 'm':'n', 'n':'o', 'o':'p', 'p':'q', 'q':'r', 'r':'s', 's':'t', 't':'u', 'u':'v', 'v':'w', 'w':'x', 
                    'x':'y', 'y':'z', 'z':'a', '-':' ', ' ':' '}

    deciphered_name = room[0]
    for i in range(room[1]):
        for i, c in enumerate(deciphered_name):
            deciphered_name[i] = decript_dict[deciphered_name[i]]
        
    return ''.join(deciphered_name)


def main():
    data = get_data()
    rooms = clean_data(data)
    sum = 0
    for room in rooms:
        sum += room[1]
        t = decipher_room_name(room)

        if 'north' in t:
            print(t, room[1])
        
    print(sum)
    

if __name__ == '__main__':
    main()

