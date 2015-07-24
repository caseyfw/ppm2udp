# Requires bitstring module
# $ pip install bitstring

import socket
from time import sleep
from bitstring import Bits

UDP_ADDR = "10.0.0.9"
UDP_PORT = 5040

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    for servo_value in range(0,1000):
        bits = Bits('uint:16=' + str(servo_value))
        print bits.bin
        s.sendto(bits.tobytes(), (UDP_ADDR, UDP_PORT))
        sleep(0.1)
