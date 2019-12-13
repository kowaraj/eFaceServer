import socket, sys
import threading
import time

HOST, PORT = "localhost", 61009

def client(h, p, msg):
    data = " ".join(sys.argv[1:]) + ' --- ' + msg
    print("data = {}".format(data))


    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((h, p))
        sock.sendall(bytes(data + "\n", encoding='utf8'))
        received = str(sock.recv(1024))

    finally:
        sock.close()

    print("Sent:     {}".format(data))
    print("Received: {}".format(received))

if __name__ == "__main__":

    t1 = threading.Thread(target=client, args=[HOST, PORT, "message 1"])
    t2 = threading.Thread(target=client, args=[HOST, PORT, "message 2"])
    t3 = threading.Thread(target=client, args=[HOST, PORT, "message 3"])

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    print('Every thread has joined. Exit.')


