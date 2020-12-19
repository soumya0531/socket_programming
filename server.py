import socket
from _thread import *
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
server.bind(('localhost',8000))
server.listen(1)
list_clients=[]
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
while True:
    conn,adrr=server.accept()
    list_clients.append(conn)
    print("connected"+adrr[0])
    start_new_thread(clientthread,(conn,adrr))
conn.close()
server.close()