import socket

def main():

	host = '127.0.0.1'
	port = 5000

	sockobj = socket.socket()
	sockobj.connect((host, port))

	message = input("->")

	while message != 'q':

		sockobj.send(message.encode())

		data = sockobj.recv(1024)

		print("Data received from Server: " + str(data.decode()))

		message = input("->")

	sockobj.close()

if __name__ == '__main__':
		main()	