import socket

def main():
	host = '127.0.0.1'
	port = 5000

	sockobj = socket.socket()
	sockobj.bind((host, port))
	sockobj.listen(1)
	connec, addr = sockobj.accept()
	print ("Connection from: " + str(addr))
	while True:
		data = connec.recv(1024)
		data = data.decode()
		if not data:
			break
		print ("From connected user: " + str(data))
		data = str(data).upper()
		print ("Sending data: " + str(data))
		connec.send(data.encode())
	connec.close()

if __name__ == '__main__':
			main()		