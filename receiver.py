# Requires bitstring module
# $ pip install bitstring

import socket
from bitstring import ConstBitStream

UDP_BIND_IP = "127.0.0.1"
UDP_PORT = 5040

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((UDP_BIND_IP, UDP_PORT))

while True:
    data = s.recv(1024)
    length = len(data) * 8
    if length < 16:
        continue

    bits = ConstBitStream(bytes=data, length=length)
    print "Received: ", data
    print "Bits:", bits.bin
    while bits.pos <= length - 16:
        servo, value = bits.readlist('uint:7, int:9')
        print "Servo: ", servo, "Value: ", value
