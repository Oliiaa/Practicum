import socket, threading
import sys


def accept_client():
    while True:
        cli_sock, cli_add = ser_sock.accept()
        CONNECTION_LIST.append(cli_sock)

        thread_client = threading.Thread(target=broadcast_usr, args=[cli_sock, cli_add])
        thread_client.start()


def broadcast_usr(cli_sock, cli_add):
    with open("info.txt", "a") as f_id:
        f_id.write(cli_add[0] + " ")
        f_id.write(str(cli_add[1]) + '\n')
    print('Хотите использовать команды для серевра Y/N')
    s = input()
    flag_his = False
    flag_clear_his = False
    flag_id = False
    msg_to_do = ''
    while True:
        if s == 'Y':
            msg_to_do = input('Введите что вы хотите сделать: ')
        if msg_to_do == 'Показывать сообщения':
            flag_his = True
        elif msg_to_do == 'Очистить сообщения':
            flag_clear_his = True
        elif msg_to_do == 'Очистить файл с информацией':
            flag_id = True
        try:
            data = cli_sock.recv(1024)
            with open("history.txt", "a") as f_his:
                f_his.write(str(data.decode()))
                f_his.write('\n')
            if flag_his:
                print(data.decode()+'\n')
            if flag_clear_his:
                with open("history.txt", 'w') as f_his:
                    f_his.write("")
                flag_his = False
            if flag_id:
                with open("info.txt", "w") as f_id:
                    f_id.write("")
                    flag_id = False
            if data:
                b_usr(cli_sock, data)
        except Exception as x:
            print(x.message)
            break


def b_usr(cs_sock, msg):
    for client in CONNECTION_LIST:
        if client != cs_sock:
            client.send(msg)


if __name__ == "__main__":
    CONNECTION_LIST = []

    ser_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    HOST = 'localhost'
    PORT = 7777
    ser_sock.bind((HOST, PORT))

    ser_sock.listen(1)
    print('Используется порт : ' + str(PORT))
    thread_ac = threading.Thread(target=accept_client)
    thread_ac.start()