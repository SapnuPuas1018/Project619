"""
author - Yuval Hayun
date   - 21/02/2024
"""

import socket
from tqdm import tqdm

IP = '127.0.0.1'


def scan_port(port):
    """
    checks if a specific port on the specified IP address is open.
    if the port is open then it prints the port's name

    :param port: The port number to be scanned.
    :type port: int

    :return: None
    :rtype: None

    """
    try:
        my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        my_socket.settimeout(0.5)
        result = my_socket.connect_ex((IP, port))
        if result == 0:
            print(port)
    except socket.error as err:
        print('socket error : ' + str(err))
    finally:
        my_socket.close()


def main():
    """
    main Function
    """
    for port in tqdm(range(20, 1025)):
        scan_port(port)


if __name__ == "__main__":
    main()
