import socket

def main():

	host = '127.0.0.1'
	port = 5001

	server = ('127.0.0.1', 5000)
	sockobj = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

	sockobj.bind((host, port))

	message = input("->")

	while message != 'q':
		
		sockobj.sendto(message.encode(), server)

		data, addr = sockobj.recvfrom(1024)

		print("Received from server: " + str(data.decode()))

		message = input("->")

	sockobj.close()

if __name__ == '__main__':
		main()