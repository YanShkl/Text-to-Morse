import sys
from files import welcome, MORSE_CODE_DICT

print(f'\n{welcome}') # Showing welcome ASCII

is_working=True

while is_working:

    text = input('\nInput text You want to translate to morse code or "EXIT" to exit: ').upper()

    enc_word = []

    def text_to_morse():

        for letter in text:

            if text == 'EXIT':
                global is_working

                print('You have exited the program.')
                is_working = False
                break

            if letter != ' ':
                try:
                    enc_word.append(f'{MORSE_CODE_DICT[letter]}')

                except KeyError:
                    print(f'You have entered not allowed symbol/letter: {sys.exc_info()[1]}. \n'
                          f'Please enter only English letters next time, without special symbols.')
                    break
    text_to_morse()

    print(f" Your morse code is: {' '.join(enc_word)}")