import socket
import threading

def receivedata(s):
    try:
        while True:
            data = s.recv(1024)
            data = data.decode()
            print(data)
            if(data == "ATTENDANCE-SUCCESS"):
                s.close()
    except:
        s.close()                       
def main():
    host = '127.0.0.1'
    port = 5000
    sockobj = socket.socket()
    sockobj.connect((host, port))
    rollno = input("Please Enter your rollno to initiate the connection: MARK-ATTENDANCE ROLLNUMBER")
    sockobj.send((str(rollno).encode()))
    threading.Thread(target = receivedata, args = (sockobj, )).start()
    while True:
        message = input()
        sockobj.send(message.encode())
    sockobj.close()

if __name__ == '__main__':
        main()  