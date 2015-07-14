# Requires bitstring module
# $ pip install bitstring

import socket
from time import sleep
from bitstring import ConstBitStream

UDP_ADDR = "127.0.0.1"
UDP_PORT = 5040

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    s.sendto('BZ', (UDP_ADDR, UDP_PORT))
    sleep(1)
