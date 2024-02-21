import socket
from tqdm import tqdm
import concurrent.futures

IP = '127.0.0.1'


def scan_port(port):
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
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as runner:
        runners_list = []
        for port in tqdm(range(20, 1025)):
            runners_list.append(runner.submit(scan_port, port))
        concurrent.futures.wait(runners_list)


if __name__ == "__main__":
    main()
