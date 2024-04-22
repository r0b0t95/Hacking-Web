import socket
from colorama import Fore

# colores
blue = Fore.GREEN
red = Fore.RED
magenta = Fore.MAGENTA
yellow = Fore.YELLOW

target_ip = '192.168.23.131'
ports = [8083, 8089, 443]


def main(target, port):
    try:
        # protocolo TCP
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        s.settimeout(0.5)

        if not s.connect_ex((target, port)):
            print(magenta + f'[+] Puerto {port} abierto')
        else:
            print(blue + f'[*] Puerto {port} cerrado')

        # cerrar conexion
        s.close()

    except socket.error:
        print(red + '[-] Error... :(')


if __name__ == '__main__':
    print(yellow + '[+] Escaneando... :)')

    for port in ports:
        main(target=target_ip, port=port)

