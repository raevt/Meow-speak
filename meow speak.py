"""
    Author: Rae Adimer (User:Vermont)
    Converts English text to Meow-speak, and the other way
    This is painfully inefficient but meh
"""

def _flip_dict(input: dict) -> dict:
    """
    Invert the keys and values of a dictionary.
    """
    # See https://stackoverflow.com/a/483685
    return dict((v, k) for k, v in input.items())

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

binary_to_meow_dict = {
    '0': 'meow ',
    '1': 'mew ',
    'W': 'mau ',
    'X': 'Mreow ',
    'Y': 'Mreeow ',
    'Z': 'Mreeeow ',
}

decode_dict = _flip_dict(encode_dict)

meow_to_binary_dict = _flip_dict(binary_to_meow_dict)

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
