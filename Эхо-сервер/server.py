import socket
sock = socket.socket()
import random
connected_users = []

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

while True:
	try:
		port = 9090
		sock.bind(('', port))
		break
	except:
		port = random.randint(1024,65535)
		sock.bind(('', port))

sock.listen(0)
print("Используется порт: ", port)

msg = ''
while True:
	conn, addr = sock.accept()
	connected_users.append(conn)
	strok = str(addr[0])
	passwd0 = conn.recv(128)
	s = 'N'.encode()
	passwd = str(passwd0.decode()) + '\n'
	with open('info.txt', 'r', encoding='utf-8') as file:
		for line in file:
			line1 = line.split(';')
			if strok == line1[0] and passwd == line1[1]:
				print("Здравствуйте", addr[0], '!')
				break
		else:
			send_msg = 'У вас есть учетная запись? Y/N'
			conn.send(send_msg.encode())
			s = conn.recv(1024)
			if s.decode() == 'Y':
				conn.send('Ошибка входа'.encode())
	if s.decode() == 'N':
		with open('info.txt', 'a', encoding='utf-8') as file:
			file.write(str(addr[0]) + ';' + str(passwd))
	with open('connect.txt', 'a', encoding='utf-8') as file:
		file.write(str(addr) + '  ' + 'connected\n')
	while True:
		data = conn.recv(1024)
		if not data:
			break
		msg = data.decode()
		if msg != 'client disconnected':
			print(addr, msg)
			for user in connected_users:
				if conn != user:
					temp = str(addr) + str(msg)
					user.send(temp.encode())
		else:
			with open('connect.txt', 'a', encoding='utf-8') as file:
				file.write(str(addr) + '  ' + 'disconnected\n')
				try:
					connected_users.remove(conn)
				except:
					break
	conn.close()