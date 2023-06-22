#!/usr/bin/env python3

"""
    Rae Adimer
    Meow-speak 2
"""

characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ',', ':', ';', "'", '"', '-', '–', '—', '(', ')', '[', ']', '…', ' ', '.', '?', '!']
meow_dict = {
        '0': 'meow ',
        '1': 'mew ',
        '2': 'mreow ',
        '3': 'nyaa ',
        '4': 'mewl ',
        '5': 'mau ',
    }

def setup():
    combos = []
    for a in characters:
        for b in characters:
            if f'{a}{b}' not in combos:
                combos.append(f'{a}{b}')
    counter = 0
    code_dict = {}
    for n in combos:
        code_dict[str(n)] = str(decimal_to_senary(counter))
        counter += 1
    return code_dict

def decimal_to_senary(num):
    num = int(num)
    if num >= 7776:
        print('Number too large')
        return
    senary = [0, 0, 0, 0, 0]
    places = [1296, 216, 36, 6, 1]
    num_rem = num
    for place in places:
        while num_rem >= place:
            num_rem = num_rem - place
            senary[places.index(place)] += 1
    converted = ''
    for n in senary:
        converted += str(n)
    return(converted)

def encode(text, code_dict):
    # Example: Hello my name is meow
    if len(text) % 2 != 0:
        text += ' '
    pairs = []
    check = 0
    to_add = ''
    for n in text:
        if check == 1:
            to_add += n
            pairs.append(to_add)
            check = 0
            to_add = ''
        else:
            to_add += n
            check = 1
    meow = ''
    for n in pairs:
        meow += encode_pair(n, code_dict)
    return meow

def encode_pair(pair, code_dict):
    senary = code_dict[pair]
    meow = ''
    for n in senary:
        meow += meow_dict[n]
    return meow

def flip_dict(input: dict) -> dict:
    # Invert the keys and values of a dictionary: from tomodachi94
    # See https://stackoverflow.com/a/483685
    return dict((v, k) for k, v in input.items())

def decode(text, code_dict):
    decode_dict = flip_dict(code_dict)
    decode_meow = flip_dict(meow_dict)
    text_list = text.split(' ')
    pairs_coded = []
    counter = 0
    to_add = ''
    for n in text_list:
        if counter != 4:
            to_add += n + ' '
            counter += 1
        elif counter == 4:
            to_add += n
            pairs_coded.append(to_add)
            to_add = ''
            counter = 0
    pairs_decoded = []
    for n in pairs_coded:
        pairs_decoded.append(decode_pair(n, decode_dict, decode_meow))
    text_final = ''
    for n in pairs_decoded:
        text_final += n
    return text_final

def decode_pair(string, decode_dict, decode_meow):
    # something like: 'meow meow meow meow meow'
    string_list = string.split(' ')
    decode_num = ''
    for n in string_list:
        decode_num += decode_meow[f'{n} ']
    decoded = decode_dict[decode_num]
    return decoded
    

def main():
    code_dict = setup()
    again = True
    while again == True:
        move = False
        while move == False:
            mode = str(input('Encode (e) or decode (d): '))
            if mode == 'e' or mode == 'd':
                move = True
            else:
                print('Invalid mode')
        text = str(input('Enter text to be converted: '))
        if mode == 'e':
            meow = encode(text.lower(), code_dict)
        elif mode == 'd':
            meow = decode(text, code_dict)
        print('---------------\nConverted text:')
        print(meow)
        prompt = str(input('Convert another text (y/n): '))
        if prompt == 'n':
            again = False

if __name__ == "__main__":
    main()