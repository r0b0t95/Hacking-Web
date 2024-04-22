#!/usr/bin/python3
# r0b0t95
# URL Encode and Decode
import argparse
from urllib.parse import quote, unquote
from colorama import Fore

# colors
blue = Fore.GREEN
red = Fore.RED
magenta = Fore.MAGENTA
yellow = Fore.YELLOW


def encode_decode(text, argv):
    if argv.e:
        encode_url = quote(text)
        return encode_url
    elif argv.d:
        decode_url = unquote(text)
        return decode_url
    else:
        return '[-] Error the argument could be -e or -d'


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-e', action='store_true', help='encode')
    parser.add_argument('-d', action='store_true', help='decode')
    txt = input(yellow + 'type: ')
    arg = parser.parse_args()
    print(blue + encode_decode(txt, arg))


if __name__ == '__main__':
    main()
