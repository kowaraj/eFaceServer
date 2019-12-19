import socketserver
import time
import threading    
import random 
import FidzStatus

class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):

    def handle(self):
        data = str(self.request.recv(1024))
        print('request received: ' + data)

        r = bytearray(b'eAS01\x00\x00\x00\x02\x00\x02\x00\x0b\x02\x00\x00\x00\x01\x00\x01\x00\x00\x01\x00\x00\x00\x00\x02\tSESSIONID\x02\x00\x00\x00\x01\x00\x00\x00\x00\x08\x00\x00\x00Welcome.')        
        print('length = ' + str(len(r)))
        self.request.sendall(r)

        print('\n2. Waiting to continue..........')
        data = str(self.request.recv(1024))
        print('request received: ' + data)
        r = bytearray(b'eAS0\x1a\x00\x00\x00\x02\x00\x02\x00\x0b\x02\x00\x00\x00\x05\x00\x01\x00\x00\x01\x00\x00\x00\x00\x02\x00\r\x02\x00\x00\x00\x01\x00')
        print('length = ' + str(len(r)))
        self.request.sendall(r)

        print('\n3. Waiting to continue..........')
        data = str(self.request.recv(1024))
        print('request received: ' + data)
        
        fs = FidzStatus.Status()
        r = fs.getReport()
        self.request.sendall(r)


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