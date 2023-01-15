import socket

ip_address = "127.0.0.1"
port = 1234

cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

cs.connect((ip_address, port))

msg = input("Enter Msg to send :")

while msg!='quit':
    cs.send(msg.encode())
    msg = cs.recv(1024).decode()
    print(msg)
    msg = input("Enter Msg to send :")

cs.close()