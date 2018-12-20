import socket
import threading
from random import randint
def thfunc(sockobj, i):
	randomnum = randint(0,50)
	connec, addr = sockobj.accept()
	print("Connection from: " + str(addr))
	print("Random number: " + str(randomnum))
	guesses = 0
	while True:
		guesses = guesses + 1
		data = connec.recv(1024)
		data = data.decode()
		data = int(data)
		if not data:
			break
		print("Data from connected user " + str(i) +" : " + str(data))
		if data	< randomnum:
			connec.send("Your guess is less than the random num".encode())
		if data > randomnum:
		    connec.send("Your guess is greater than the random num".encode())
		if data == randomnum:
		    connec.send(("Hurray!!! You guessed it in " + str(guesses) +" guesses").encode())
		    connec.close()
		    return   


def main():

	totalconnec = int(input("Please provide number of users: "))

	host = '127.0.0.1'
	port = 5000
	
	sockobj = socket.socket()
	
	sockobj.bind((host, port))
	
	sockobj.listen(1)
	
	threadarr = list()
	for i in range(0, totalconnec):
	    thread = threading.Thread(target = thfunc, args = (sockobj, i))
	    threadarr.append(thread)
	    threadarr[i].start()    
	for i in range(0, totalconnec):
	    threadarr[i].join()

	print("CHAITU SERVER ----> Done for the Day!!!")

if __name__ == '__main__':
	       	main()	       


