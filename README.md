# socket_programming

Build a simple client-server system, where you use the
client to chat with a dummy server. The protocol between the client and server is
as follows.
• The server is first started on a known port.
• The client program is started (server IP and port are provided on the
command line).
• The client connects to the server, and then asks the user for input. The user
types his message on the terminal (e.g., "Hi", "Bye", "How are you"). The
user's input is sent to the server via the connected socket.
• The server reads the user's input from the client socket. If the user has typed
"Bye" (without the quotes), the server must reply with "Goodbye". For any
other message, the server must reply with "OK".
• The client then reads the reply from the server and checks that it is accurate
(either "OK" or "Goodbye").
• If the user had typed "Bye", and the server replied with a "Goodbye"
correctly, the client quits. Otherwise, the client asks the user for the next
message to send to the server.
You will write the client and server code to communicate with each other.

The client
You will write a simple client in a file called "client.c". Below is a sample run of
the client. For this example, the client code is first compiled. Then a server is run
on port 5000 in another terminal. The client program is then given the server IP
(127.0.0.1 in this case, which is a special IP address that always points to the local
machine) and port (5000) as command line inputs. When the user enters messages
like Hello or Hi, the server replies with OK. When the user says Bye, the server
says Goodbye. The client program will exit after user enters "Bye" and server
replies "Goodbye".
In another run of the client, we show what happens when the server sends a wrong
reply, say, "NO" instead of "OK". Here, the client exits with error message. This
behavior should not happen with your server code.
$ ./client 127.0.0.1 5000
Connected to server
Please enter the message to the server: Hello
Server replied: NO
ERROR wrong reply from server

The server
Now, you will write a simple server in a file called "server.c". The server program
should take the port number from the command line and start a listening socket on
that command line. Whenever a client request arrives on that socket, the server
should accept the connection, and store the client socket. The server must then read
from the socket. When the client has sent a message, the server should reply "OK"
or "Goodbye" based on what the client has sent. After replying to one message, the
server should then wait to read the next message from the client.
Note that your simple server will not handle multiple clients concurrently. That is,
when the server is engaged with a client, another client that tries to chat with the
same server will see an error message. You may verify this during your
implementation and testing.
Below is sample output from our version of server (corresponding to the client
output shown above). Your server should produce similar output (the exact words
printed in the statements may differ). Note that our server is printing out the client
socket file descriptor number for debugging.
