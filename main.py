import sys
from files import welcome, MORSE_CODE_DICT  # importing data with welcoming logo and morse dictionary

print(f'\n{welcome}')  # Showing welcome ASCII

is_working = True

while is_working: # Loop what drive work of program

    text = input('\nInput text You want to translate to morse code or "EXIT" to exit: ').upper()

    enc_word = []


    def text_to_morse():

        for letter in text: # Iterating trough each letter

            if text == 'EXIT': # key word for exiting the program
                global is_working

                print('You have exited the program.')
                is_working = False
                break

            if letter != ' ':
                try:
                    enc_word.append(f'{MORSE_CODE_DICT[letter]}')

                except KeyError:
                    print(f'You have entered not allowed symbol/letter: {sys.exc_info()[1]}. \n'
                          f'Please enter only English letters next time, without special symbols(i.e.^@*~)')
                    continue


        print(f" Your morse code is: {' '.join(enc_word)}")


    text_to_morse()


