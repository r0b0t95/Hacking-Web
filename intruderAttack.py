#!/usr/bin/python3
import requests as req
import sys
import signal

def def_handler(sig, frame):
     print('\n[!] Stopping th process...\n')
     sys.exit(1)

# Ctrl + C
signal.signal(signal.SIGINT, def_handler)

file_txt = 'intruderTxt.txt'
word_list = open(file_txt, 'r')

def fuzzing():
     word_list.readline()
     for word in word_list:
          target = 'https://0a5100330377989b833ba37800670055.web-security-academy.net/?search=%s' % (word.strip())
          r = req.get(url=target)
          print(r.status_code)
          if r.status_code == 200:
               print(word)

def closeConnections():
     word_list.close()
     

if __name__ == '__main__':
     fuzzing()
     closeConnections()