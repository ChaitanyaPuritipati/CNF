import socket

def main():

	host = '127.0.0.1'
	port = 5000

	sockobj = socket.socket()
	sockobj.connect((host, port))

	print("Game Started!!! Let's start guessing the number")
	message = input("Your number ->")

	while message != 'q':

		sockobj.send(message.encode())

		data = sockobj.recv(1024)

		print("Data received from Server: " + str(data.decode()))

		check = str(data.decode()).split(" ")

		if check[0] == "Hurray!!!":
			print("Thanks for Playing :)")
			sockobj.close()
			return
		message = input("Your number ->")
	sockobj.close()

if __name__ == '__main__':
		main()	