import random 


class Status():


    def __to_hexb(self, len):
        if len > 0xFFFF:
            print("Message is too big, len > 2^16")
            exit(-1)

        len_hex = "{0:04x}".format(len)
        b = bytearray.fromhex(len_hex)
        b.reverse()
        print("to_hexb: " + str(b))
        return b

    def getReplyOnMsgType1(self, data):
        print('request received: ' + data)
        r = bytearray(b'eAS01\x00\x00\x00\x02\x00\x02\x00\x0b\x02\x00\x00\x00\x01\x00\x01\x00\x00\x01\x00\x00\x00\x00\x02\tSESSIONID\x02\x00\x00\x00\x01\x00\x00\x00\x00\x08\x00\x00\x00Welcome.')        
        print('length = ' + str(len(r)))
        return r

    def getReplyOnMsgType5(self, data):
        print('request received: ' + data)
        r = bytearray(b'eAS0\x1a\x00\x00\x00\x02\x00\x02\x00\x0b\x02\x00\x00\x00\x05\x00\x01\x00\x00\x01\x00\x00\x00\x00\x02\x00\r\x02\x00\x00\x00\x01\x00')
        print('length = ' + str(len(r)))
        return r

    def getReplyOnMsgType6(self, data):
        print('request received: ' + data)
        b0= b'eAS0'
        b1= b'\x00\x00\x02\x00\x02\x00\x0b\x02\x00\x00\x00\x06\x00\x01\x00\x00\x01\x00\x00\x00\x01\x02\x00\r\x02\x00\x00\x00\x01\x00\x05\x00\x04'
        b2= b'\x00\x00\x02\x00\x05\x02\x00\x00\x00\xff\x01\x01\x00\x06\x01\x00\x00\x00\x02\x03\x00\x07\x04\x00\x00\x00\x02\x00\x00\x00\x02\x05ERROR\x02\x00\x00\x00\x00\x00\x02\x00\r\x02\x00\x00\x00\x01\x00\x03\x08DATATIME\x04\x00\x00\x00\x00\x00\x00\x00\x02\x00\x08'
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

        r = bytearray(b0 + self.__to_hexb(l1) + b1 + self.__to_hexb(l2) + b2 + self.__to_hexb(l3) + b3 + b4)
        print('r      = ' + str(r))
        print('length = ' + str(len(r)))

        return r


