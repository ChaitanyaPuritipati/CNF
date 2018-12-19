import socket

def convert(convdata, val):
	convdict = { "Dollar-INR":67,
	             "Dollar-Pounds":0.75,
	             "Dollar-Yen":113.41,
	             "INR-Dollar": 0.0149,
	             "Pounds-Dollar": 1.3333,
	             "Yen-Dollar": 0.0088
	}

	return round(val * convdict[convdata], 1)

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

		splitdata = data.split(" ")

		data = convert(splitdata[1] + "-" + splitdata[4], int(splitdata[2]))

		print("Sending data: " + str(data))
		
		sockobj.sendto(str(data).encode(), addr)

	sockobj.close()

if __name__ == '__main__':
			main()		

        