alphabet_latin = '_0123456789ABCDEFGHIKLMNOPQRSTVXYZ'
alphabet_kirillica = '_0123456789АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'


def endecryption(type, alphabet, text, key):
    encry_text = ''
    for i in text:
        try:
            up_alf = i.upper()
            if up_alf in alphabet:
                index = alphabet.index(up_alf)
                if type == 1:
                    encry_text += alphabet[int(index - key)]
                elif type == 2:
                    if int(index + key) >= len(alphabet)-1:
                        encry_text += alphabet[index + key - len(alphabet)]
                    else:
                        encry_text += alphabet[index + key]
        except ValueError:
            print('Неверный выбор алфавита или кодировка текста')
    print(encry_text)

type_oper = int(input('Введите тип операции'))

alph_input = int(input('Введите номер алфавита'))

if alph_input == 1:
    alph = alphabet_latin
    print('Выбрана латиница')
elif alph_input == 2:
    alph = alphabet_kirillica
    print('Выбрана кириллица')
else:
    print('U stupid?')

text_input = input('Введите тект для шифрования')

key_input = int(input('Введите ключ'))

endecryption(type_oper, alph, text_input, key_input)
