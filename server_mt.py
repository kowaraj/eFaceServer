import socketserver
import time
import threading    
import random 

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

def to_hexb(len):
    if len > 0xFFFF:
        print("Message is too big, len > 2^16")
        exit(-1)

    len_hex = "{0:04x}".format(len)
    b = bytearray.fromhex(len_hex)
    b.reverse()
    print("to_hexb: " + str(b))
    return b


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
        
        b0= b'eAS0'
        b1= b'\x00\x00\x02\x00\x02\x00\x0b\x02\x00\x00\x00\x06\x00\x01\x00\x00\x01\x00\x00\x00\x01\x02\x00\r\x02\x00\x00\x00\x01\x00\x05\x00\x04'
        b2= b'\x00\x00\x02\x00\x05\x02\x00\x00\x00\xff\x01\x01\x00\x06\x01\x00\x00\x00\x02\x03\x00\x07\x04\x00\x00\x00\x02\x00\x00\x00\x02\x05ERROR\x02\x00\x00\x00\x00\x00\x02\x00\r\x02\x00\x00\x00\x01\x00\x03\x08DATATIME\x04\x00\x00\x00\x00\x00\x00\x00\x02\x00\x08'
        b3= b'\x00\x00echofep GIT_VER.0.90localhost localhost -  2019-350.14:20:08\neAssSrvr: CommandCnt: 1 ReplyCnt: 0 RepliesPosted: 0 ReplyPolls: 0 Accepts: 1 Connections: 1\nRate: 666.8 Mbits/s123456789'
        b4= b'\n\x00'

        b3= \
'''\x00\x00fidx 26c.0.52 pcposc1 -  2019-350.18:20:05    Log: pcposc1:/Data/log/fidx_ams_current.log
eAssSrvr: CommandCnt: 1 ReplyCnt: 0 RepliesPosted: 0 ReplyPolls: 0 Accepts: 1 Connections: 1
Source: pcposc0.cern.ch Counters cleared 03h:57:09 pty Errs 0  State: Idle 1 secs
   Path                    Source   Target   To_Go Since     Delay
F0 /Data/FRAMES/HKHR/RT    3658/599 3658/599   -   00:26     02:05
F1 /Data/FRAMES/HKBPB/RT   4241/075 4241/075   -   00:26     22:00
F2 /Data/FRAMES/SCIBPB/RT  4244/052 4244/052   -   00:24     22:05
F3 /Data/FRAMES/SCI/RT     0014/090 0014/090   -    -         -
F4 /Data/FRAMES/HKRBPB/RT  0063/814 0063/814   -    -        14d:13:33
F5 /Data/FRAMES/HKRPB/RT   0072/144 0072/144   -    -        14d:13:33
F6 /Data/FRAMES/SCIRBPB/RT 0062/347 0062/347   -    -        14d:13:33
F7 /Data/FRAMES/SCIRPB/RT  None     None       -    -         -
F8 /Data/FRAMES/HKLR/CDP   3670/495 3670/495   -   00:24     Current  
F9 /Data/FRAMES/P2PRP/RT   0010/102 0010/102   -    -        10h:08:44
Rate: {0} Mbits/s
'''.format(random.randint(1, 100) ).encode()

        print('len b0 = ' + str(len(b0)))
        print('len b1 = ' + str(len(b1)))
        print('len b2 = ' + str(len(b2)))
        print('len b3 = ' + str(len(b3)))
        print('len b4 = ' + str(len(b4)))
        
        l1 = len(b1 + b2 + b3 + b4)
        print('l1 = ' + str(l1))
        l2 = len(     b2 + b3 + b4)
        print('l2 = ' + str(l2))
        l3 = len(          b3     )
        print('l3 = ' + str(l3))

        r = bytearray(b0 + to_hexb(l1) + b1 + to_hexb(l2) + b2 + to_hexb(l3) + b3 + b4)
        print('r      = ' + str(r))
        print('length = ' + str(len(r)))

        # r_ = bytearray(b'eAS0\x23\x01\x00\x00\x02\x00\x02\x00\x0b\x02\x00\x00\x00\x06\x00\x01\x00\x00\x01\x00\x00\x00\x01\x02\x00\r\x02\x00\x00\x00\x01\x00\x05\x00\x04\x02\x01\x00\x00\x02\x00\x05\x02\x00\x00\x00\xff\x01\x01\x00\x06\x01\x00\x00\x00\x02\x03\x00\x07\x04\x00\x00\x00\x02\x00\x00\x00\x02\x05ERROR\x02\x00\x00\x00\x00\x00\x02\x00\r\x02\x00\x00\x00\x01\x00\x03\x08DATATIME\x04\x00\x00\x00\x00\x00\x00\x00\x02\x00\x08\xb7\x00\x00\x00echofep GIT_VER.0.90localhost localhost -  2019-350.14:20:08\neAss---Srvr: CommandCnt: 1 ReplyCnt: 0 RepliesPosted: 0 ReplyPolls: 0 Accepts: 1 Connections: 1\nRate: 666.8 Mbits/s12345\n\x00')
        # print('r      = ' + str(r_))
        # print('length = ' + str(len(r_)))
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