#!/usr/bin/python3
#r0b0t95
import socket

def scan_port(host, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        result = s.connect_ex((host, port))
        if result == 0:
            print(f"Port {port} is open")
        else:
            print(f'Port {port} is close')
    except socket.error:
        print('[-] Error ...')


if __name__ == "__main__":
    host = '192.168.23.129'
    port = 8000
    scan_port(host=host, port=port)

