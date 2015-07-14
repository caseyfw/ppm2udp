# Requires bitstring module
# $ pip install bitstring

import socket
from time import sleep
from bitstring import Bits

UDP_ADDR = "127.0.0.1"
UDP_PORT = 5040

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    for servo_value in range(-255, 256):
        bits = Bits('uint:7=0, int:9=' + str(servo_value) + ', uint:7=1, int:9=' + str(servo_value))
        print bits.bin
        s.sendto(bits.tobytes(), (UDP_ADDR, UDP_PORT))
        sleep(0.1)
