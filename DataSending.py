import Encoder
from FreeD import FreeD, FreeDWrapper
import socket
from time import sleep
from threading import Thread



class SendData(Thread):

    def SendFreeDData(IP, Port):
        MULTICAST_TTL = 2
        MCAST_GRP = '224.1.1.1'

        print ("Sending Data")
        struct = FreeDWrapper(0,0,0,0,0,0,0,0)
        bits: 'bytes' = struct.createFreeD().encode()
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, MULTICAST_TTL)
        sock.bind((MCAST_GRP, Port))

        while True:

            struct.focus = abs(Encoder.counter)
            bits = struct.createFreeD().encode()


            sock.sendto(bits, (MCAST_GRP, Port))
            sleep(1/60)