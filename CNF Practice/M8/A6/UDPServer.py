import socket

def main():
	host = '127.0.0.1'
	port = 5000

	sockobj = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

	sockobj.bind((host, port))

	print("Server Started!!!")

	while True:
		data, addr = sockobj.recvfrom(1024)
		data = data.decode()
		print("Data received from: " + str(addr))
		print("Data from client: " + str(data))
		data = str(data).upper()
		print("Sending data: " + str(data))
		sockobj.sendto(data.encode(), addr)
	sockobj.close()

if __name__ == '__main__':
		main()	
