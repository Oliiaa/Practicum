import socket, threading
import sys


def send(uname):
    while True:
        msg = input('\nя сказал(a): ')
        if msg == "exit":
            cli_sock.close()
            data = uname + ' покинул нас'
            sys.exit()
        else:
            data = uname + ' сказал(a): ' + msg
            cli_sock.send(data.encode())


def receive():
    while True:
        data = cli_sock.recv(1024)
        print('\t' + str(data.decode()))


if __name__ == "__main__":
    cli_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    HOST = 'localhost'
    PORT = 7777

    uname = input('Введите имя для отображения в чате:  ')

    cli_sock.connect((HOST, PORT))
    print('Connected to remote host...')

    thread_send = threading.Thread(target=send, args=[uname])
    thread_send.start()

    thread_receive = threading.Thread(target=receive)
    thread_receive.start()