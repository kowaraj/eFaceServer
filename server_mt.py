import socketserver
import time
import threading    
import random 
import FidzStatus

# bytearray(b'eAS01\x00\x00\x00\x02\x00\x02\x00\x0b\x02\x00\x00\x00\x01\x00\x01\x00\x00\x01\x00\x00\x00\x00\x02\tSESSIONID\x02\x00\x00\x00\x01\x00\x00\x00\x00\x08\x00\x00\x00Welcome.')
# >>> s1 = "0x65 0x41 0x53 0x30 0x1a 0x00 0x00 0x00 0x02 0x00 0x02 0x00 0x0b 0x02 0x00 0x00 0x00 0x05 0x00 0x01 0x00 0x00 0x01 0x00 0x00 0x00 0x00 0x02 0x00 0x0d 0x02 0x00 0x00 0x00 0x01 0x00"
# >>> l1 = s1.split(' ')
# >>> l1
# ['0x65', '0x41', '0x53', '0x30', '0x1a', '0x00', '0x00', '0x00', '0x02', '0x00', '0x02', '0x00', '0x0b', '0x02', '0x00', '0x00', '0x00', '0x05', '0x00', '0x01', '0x00', '0x00', '0x01', '0x00', '0x00', '0x00', '0x00', '0x02', '0x00', '0x0d', '0x02', '0x00', '0x00', '0x00', '0x01', '0x00']
# >>> b1 = [int(i,16) for i in l1]
# >>> b1
# [101, 65, 83, 48, 26, 0, 0, 0, 2, 0, 2, 0, 11, 2, 0, 0, 0, 5, 0, 1, 0, 0, 1, 0, 0, 0, 0, 2, 0, 13, 2, 0, 0, 0, 1, 0]
# >>> bytearray(b1)
# bytearray(b'eAS0\x1a\x00\x00\x00\x02\x00\x02\x00\x0b\x02\x00\x00\x00\x05\x00\x01\x00\x00\x01\x00\x00\x00\x00\x02\x00\r\x02\x00\x00\x00\x01\x00')
# '\t'.join(s2)
# >>> s3.spit('\t')


#instead of: class MyTCPSocketHandler(socketserver.BaseRequestHandler):
class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):

    def handle(self):
        data = str(self.request.recv(1024))
        print('request received: ' + data)
        #cur_thread = threading.current_thread()

        #response = bytes("Replying to {}: DATA={}".format(cur_thread.name, data), encoding='utf8')
        # [101, 65, 83, 48, 49, 0, 0, 0, 2, 0, 2, 0, 11, 2, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 2, 9, 83, 69, 83, 83, 73, 79, 78, 73, 68, 2, 0, 0, 0, 1, 0, 0, 0, 0, 8, 0, 0, 0, 87, 101, 108, 99, 111, 109, 101, 46]
        # ['0x65', '0x41', '0x53', '0x30', '0x31', '0x00', '0x00', '0x00', '0x02', '0x00', '0x02', '0x00', '0x0b', '0x02', '0x00', '0x00', '0x00', '0x01', '0x00', '0x01', '0x00', '0x00', '0x01', '0x00', '0x00', '0x00', '0x00', '0x02', '0x09', '0x53', '0x45', '0x53', '0x53', '0x49', '0x4f', '0x4e', '0x49', '0x44', '0x02', '0x00', '0x00', '0x00', '0x01', '0x00', '0x00', '0x00', '0x00', '0x08', '0x00', '0x00', '0x00', '0x57', '0x65', '0x6c', '0x63', '0x6f', '0x6d', '0x65', '0x2e']

        r = bytearray(b'eAS01\x00\x00\x00\x02\x00\x02\x00\x0b\x02\x00\x00\x00\x01\x00\x01\x00\x00\x01\x00\x00\x00\x00\x02\tSESSIONID\x02\x00\x00\x00\x01\x00\x00\x00\x00\x08\x00\x00\x00Welcome.')        
        print('length = ' + str(len(r)))
        self.request.sendall(r)

        print('\n2. Waiting to continue..........')
        data = str(self.request.recv(1024))
        print('request received: ' + data)
        #cur_thread = threading.current_thread()
        r = bytearray(b'eAS0\x1a\x00\x00\x00\x02\x00\x02\x00\x0b\x02\x00\x00\x00\x05\x00\x01\x00\x00\x01\x00\x00\x00\x00\x02\x00\r\x02\x00\x00\x00\x01\x00')
        print('length = ' + str(len(r)))
        self.request.sendall(r)

        print('\n3. Waiting to continue..........')
        data = str(self.request.recv(1024))
        print('request received: ' + data)
        
        fs = FidzStatus.Status()
        r = fs.getReport()
        self.request.sendall(r)


class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass


if __name__ == "__main__":
    
    HOST, PORT = "localhost", 61009

    server = ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler)
    ip, port = server.server_address
    print("server @ {}:{}", ip, port)
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.daemon = True
    server_thread.start()

    server.serve_forever()