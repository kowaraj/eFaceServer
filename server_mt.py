import socketserver
import time
import threading    
import random 
import FidzStatus

class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):

    def handle(self):
        print('\n1. Request received.............')
        fs = FidzStatus.Status()

        data = str(self.request.recv(1024))
        r = fs.getReplyOnMsgType1(data)
        self.request.sendall(r)

        print('\n2. Waiting to continue..........')

        data = str(self.request.recv(1024))
        r = fs.getReplyOnMsgType5(data)
        self.request.sendall(r)

        print('\n3. Waiting to continue..........')

        data = str(self.request.recv(1024))
        r = fs.getReplyOnMsgType6(data)
        self.request.sendall(r)
        print('\n4. Request completed............')


class LegacyEAssServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass


if __name__ == "__main__":
    
    HOST, PORT = "localhost", 61009

    server = LegacyEAssServer((HOST, PORT), ThreadedTCPRequestHandler)
    ip, port = server.server_address
    print("server @ {}:{}", ip, port)
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.daemon = True
    server_thread.start()

    server.serve_forever()