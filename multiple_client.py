import sys
import socket
import select
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.connect(('localhost',8080))
print("Send Message to the Server=====>")
while True:
    a=""

    listed=[sys.stdin,server]
    read,write,error=select.select(listed,[],[])
    for i in read:
        if i==server:
            message=i.recv(2048)
            message=str(message)[1:][1:-1]
            sys.stdout.write("Reply By server===>")
            sys.stdout.write(message)
            sys.stdout.write("\n")
            sys.stdout.flush()
            if message=="Goodbye":
                a="yes"
                break
            else:
                pass
        else:
            message=sys.stdin.readline()
            res=message.encode('utf-8')
            server.send(res)
            sys.stdout.write("Reply to server===>")
            sys.stdout.write(message)
            sys.stdout.write("\n")
            sys.stdout.flush()
    if a=="yes":
        sys.stdout.write("\n Closing the client side")
        break
server.close()

