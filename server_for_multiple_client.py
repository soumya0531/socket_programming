import sys
import socket
import select
import os
from _thread import *
import time

def clientthread(con,adr):
    while True:
        try:
            message=con.recv(2048)
            if message:
                new_message=str(message)
                New_message=new_message[1:][1:-3]
                if New_message=="Bye":
                    m="Goodbye"
                    res=m.encode("utf-8")
                    con.send(res)
                else:
                    m="Ok"
                    res=m.encode("utf-8")
                    con.send(res)
            else:
                remove(con)
        except:
            continue
def remove(connection):
    if connection in list_clients:
        list_clients.remove(connection)

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
server.bind(('localhost',8080))
server.listen(1)
print("Server is listening at : localhost:8080")
num_of_cpus = os.cpu_count()
pid = os.getppid()
print("forking for " + str(num_of_cpus) + " cpus")
for i in range(num_of_cpus):
    n = os.fork()
    if(n > 0):
        print("Process with id : " + str(os.getppid()))
        list_clients=[]
        while True:
            conn,adrr=server.accept()
            list_clients.append(conn)
            print("connected"+adrr[0])
            start_new_thread(clientthread,(conn,adrr))
        conn.close()
        server.close()