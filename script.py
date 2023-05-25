#!/usr/bin/env python3

from re import compile, escape, sub, MULTILINE, DOTALL
from bardapi import Bard
from sys import argv
from shutil import get_terminal_size
from json import load

# put the token from the website inspection
token = '' # insert your token inside the quotes

bard = Bard(token=token)
terminal_width = get_terminal_size().columns


def ansi_code(text):
    format_codes = {
        '**': {'start': '\033[1m', 'end': '\033[0m \033[32m'},
        # '**': {'start': '\033[1m', 'end': '\033[0;32m'},
        '_': {'start': '\033[3m', 'end': '\033[0;32m'}
    }

    def add_ansi_codes(text):
        formatted_text = text

        # Iterate over the format codes and apply the corresponding ANSI escape codes
        for format_code, codes in format_codes.items():
            pattern = compile(escape(format_code) +
                              r'(.*?)' + escape(format_code))
            formatted_text = pattern.sub(
                codes['start'] + r'\1' + codes['end'], formatted_text)

        return formatted_text

    formatted_text = add_ansi_codes(text)

    # search all the '*' and display it as unicode bullet
    a = "\033[1m\033[35m \u2022 \033[0m\033[32m"

    formatted_text = sub(r'^\*', a, formatted_text, flags=MULTILINE)

    # will search all digits print on yellow
    formatted_text = sub(
        r'\b(\d+)\b', r'\033[33;1m\1\033[0;32m', formatted_text)

    # find all ``` ''' and write them on black background
    pattern = r"```(.*?)```"
    b = '-'*terminal_width
    b = f'\033[3;1;31m'+b+'\033[0;32m'
    formatted_text = sub(
        pattern, r'\n{c}\1{c}\n'.format(c=b), formatted_text, flags=DOTALL)

    return formatted_text


def print_prompt(question: str):
    '''prints the prompt on terminal'''
    # Print question in blue and bold, underlined
    print("\n -_- \033[4m\033[34m\033[1m{}\033[0m".format(
        question))


def print_response(response: str):
    '''prints the response on terminal'''
    # Print answer in white and italic
    print(">\033[32m\033[3m{}\033[0m".format(ansi_code(response)))


def get_prompt() -> str:
    ''''asks prompt from terminal'''
    print('\033[2;45m')
    print('\033[0m', end='')
    got_prompt = input('\n\033[0;1;34;2;5m>>>\033[0;4;34;1m')
    print('\033[0m')
    return got_prompt


def get_response(prompt=''):
    '''if get_response() got a prompt it will get the response for the received prompt, otherwise asks a prompt and get the response from bard'''
    if prompt == '':
        response = bard.get_answer(get_prompt())['content']
        print_response(response)
    else:
        response = bard.get_answer(prompt)['content']
        print_response(response)


def main():
    print('\033[33m\033[1m{}\033[0m'.format(
        'Google_Bard Terminal Interface by ALHAM').center(terminal_width))
    if len(argv) > 1:
        prompt = ' '.join(argv[1:])
        print_prompt(prompt)
        get_response(prompt)

    else:
        print('press \'ctl+c\' to exit from bard interface', end='')
        while True:
            get_response()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\33[31m\33[1m stopping! \33[0m')
    except Exception as e:
        print(f'An error occurred as: {e}')
