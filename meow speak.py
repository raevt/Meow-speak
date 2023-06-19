"""
    Author: Rae Adimer (User:Vermont)
    Converts English text to Meow-speak, and the other way
    This is painfully inefficient but meh
"""

encode_dict = {
    'a': '000001',
    'b': '000010',
    'c': '000011',
    'd': '000100',
    'e': '000101',
    'f': '000110',
    'g': '000111',
    'h': '001000',
    'i': '001001',
    'j': '001010',
    'k': '001011',
    'l': '001100',
    'm': '001101',
    'n': '001110',
    'o': '001111',
    'p': '010000',
    'q': '010001',
    'r': '010010',
    's': '010011',
    't': '010100',
    'u': '010101',
    'v': '010110',
    'w': '010111',
    'x': '011000',
    'y': '011001',
    'z': '011010',
    '0': '011011',
    '1': '011100',
    '2': '011101',
    '3': '011110',
    '4': '011111',
    '5': '100000',
    '6': '100001',
    '7': '100010',
    '8': '100011',
    '9': '100100',
    ',': '100101',
    ':': '100110',
    ';': '100111',
    "'": '101000',
    '‘': '101000',
    '’': '101000',
    '"': '101001',
    '“': '101001',
    '”': '101001',
    '-': '101010',
    '–': '101011',
    '—': '101100',
    '(': '101101',
    ')': '101110',
    '[': '101111',
    ']': '110000',
    '…': '110001',
    ' ': 'W',
    '.': 'X',
    '?': 'Y',
    '!': 'Z',
}

decode_dict = {
    #Because of curly quotes...it's easiest to just use two dictionaries.
    '000001': 'a',
    '000010': 'b',
    '000011': 'c',
    '000100': 'd',
    '000101': 'e',
    '000110': 'f',
    '000111': 'g',
    '001000': 'h',
    '001001': 'i',
    '001010': 'j',
    '001011': 'k',
    '001100': 'l',
    '001101': 'm',
    '001110': 'n',
    '001111': 'o',
    '010000': 'p',
    '010001': 'q',
    '010010': 'r',
    '010011': 's',
    '010100': 't',
    '010101': 'u',
    '010110': 'v',
    '010111': 'w',
    '011000': 'x',
    '011001': 'y',
    '011010': 'z',
    '011011': '0',
    '011100': '1',
    '011101': '2',
    '011110': '3',
    '011111': '4',
    '100000': '5',
    '100001': '6',
    '100010': '7',
    '100011': '8',
    '100100': '9',
    '100101': ',',
    '100110': ':',
    '100111': ';',
    '101000': "'",
    '101001': '"',
    '101010': '-',
    '101011': '–',
    '101100': '—',
    '101101': '(',
    '101110': ')',
    '101111': '[',
    '110000': ']',
    '110001': '…',
    'W': ' ',
    'X': '.',
    'Y': '?',
    'Z': '!',
}


binary_to_meow_dict = {
    '0': 'meow ',
    '1': 'mew ',
    'W': 'mau ',
    'X': 'Mreow ',
    'Y': 'Mreeow ',
    'Z': 'Mreeeow ',
}

meow_to_binary_dict = {
    'meow': '0',
    'mew': '1',
    'Mau': '',
    'mau': 'W',
    'Mreow': 'X',
    'Mreeow': 'Y',
    'Mreeeow': 'Z',
}

"""
Reminder:
    encode_dict, key is character, value is binary
    binary_to_meow_dict, key is binary or letter, value is output
"""

def encode(text):
    binary = ''
    for char in text:
        try:
            binary += encode_dict[char]
        except:
            print('Unsupported character: ' + char)
    meow = 'Mau '
    for char in binary:
        meow += binary_to_meow_dict[char]
    return meow

def decode(text):
    text_list = text.split(' ')
    binary = ''
    for n in text_list:
        try:
            binary += meow_to_binary_dict[n]
        except:
            print('Failed to convert:' + n)
    exceptions = ['W', 'X', 'Y', 'Z']
    decoded = ''
    current_decode = ''
    for n in binary:
        if n in exceptions:
            decoded += decode_dict[n]
        else:
            current_decode += n
        if len(current_decode) == 6:
            decoded += decode_dict[current_decode]
            current_decode = ''
    return decoded

def gen_list():
    #was used to make a list of all characters and their translations.
    lst_dict = {}
    lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ',', ':', ';', "'", '"', '-', '–', '—', '(', ')', '[', ']', '…']
    for n in lst:
        lst_dict[n] = str(encode(n) + '\n')
    for n in lst_dict:
        print(f'{n} = {lst_dict[n]}')

def main():
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
            meow = encode(text.lower())
        elif mode == 'd':
            meow = decode(text)
        print('---------------\nConverted text:')
        print(meow)
        prompt = str(input('Convert another text (y/n): '))
        if prompt == 'n':
            again = False


main()