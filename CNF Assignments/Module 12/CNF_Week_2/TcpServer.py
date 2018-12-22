import socket
import threading
clients = list()
rollnos = {}
question = ""
answer = ""
def thfunc(c):
    try:
        while True:
            data = c.recv(1024)
            data = data.decode()
            print(data)
            splitrollnodata = data.split(" ")
            if(splitrollnodata[0] == "MARK-ATTENDANCE"):
                if(splitrollnodata[1] not in rollnos.keys()):
                    c.send("ROLLNUMBER-NOTFOUND".encode())
                else:
                    question = rollnos[splitrollnodata[1]][0]
                    answer = rollnos[splitrollnodata[1]][1]
                    c.send(("SECRETQUESTION " + question).encode())   
            elif(splitrollnodata[0] == "SECRETANSWER"):
                if(splitrollnodata[1] == answer):
                    c.send("ATTENDANCE-SUCCESS".encode())
                    c.close()
                else:
                    c.send("ATTENDANCE FAILURE".encode())
                    c.send(("SECRETQUESTION-"+ str(question)).encode()) 
    except:
        c.close()                      
def main():
    totalconnec = int(input("Please provide number of users: "))
    host = '127.0.0.1'
    port = 5000
    sockobj = socket.socket()
    fp = open("data.csv")
    data = fp.read().splitlines()
    
    for line in data:
        splitdata = line.split(",")
        rollnos[splitdata[0]] = (splitdata[1], splitdata[2])
    sockobj.bind((host, port))
    sockobj.listen(totalconnec)
    for i in range(0, totalconnec):
        connec, addr = sockobj.accept()
        print("Connection established with " + str(addr))
        clients.append(connec)
        thread = threading.Thread(target = thfunc, args = (clients[i],))
        thread.start()  

if __name__ == '__main__':
    main()