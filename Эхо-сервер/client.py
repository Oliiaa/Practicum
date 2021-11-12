import socket
from time import sleep
from threading import Thread

#реализованы доп задания 3-10

'''Для начала необходимо ввести хост (например: 127.0.0.1), 
после этого ввести хост, 
потом ввести пароль и ответь на вопрос: "У вас есть учетная запись? Y/N"
Если дан ответ "N", то в файл info.txt будет записан новый пользователь и его пароль,
если дан ответ "Y", то имя и пароль сравниваются с лежащими в файле info.txt,  
если они не совпадают, то будет выведено сообщение: "Ошибка входа".
Если данные пользователя совпадают, то сообщение "У вас есть учетная запись? Y/N" выведено не будет.
При каждом установлении соединения информация о хосте (логин) и номер порта записывается в файл connect.txt
Каждое сообщение, написанное в клиенте отображается на сервере с указанием данных из connect.txt
'''

def check():
	while True:
		try:
			data = sock.recv(1024)
			msg = data.decode()
			print(msg)
		except:
			break


try:
	sock = socket.socket()
	x = input('Введите хост: ')
	y = int(input('Введите порт: '))
	sock.connect((x, y))
except:
	x = 'localhost'
	y = 9091
	y = 9095
	sock.connect((x, y))

msg = ''

passwd = input('Введите пароль: ')
msg = passwd
sock.send(msg.encode())

Thread(target=check).start()

while msg !="close":
	msg = input()
	if msg !='close':
		sock.send(msg.encode())




msg = 'client disconnected'
sock.send(msg.encode())

data = sock.recv(1024)

sock.close()