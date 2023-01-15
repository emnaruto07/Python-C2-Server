import socket
import threading
import time


ip_address = "127.0.0.1"
port = 1234

THREADS = []
CMD_INPUT = []
CMD_OUTPUT = []

def handle_connection():
    pass

def init_server():
    ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ss.bind((ip_address, port))
    ss.listen(5)
    connection, address = ss.accept()
    t = threading.Thread(target=handle_connection, args=(connection, address))
    THREADS.append(t)
    t.start()