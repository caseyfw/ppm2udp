import serial
import math
from bitstring import BitArray
import socket

UDP_ADDR = "10.0.0.9"
UDP_PORT = 5040
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ser = serial.Serial('/dev/tty.usbmodemfa131', 9600)

# channels = 16
# servos = [0] * channels
# min_vals = [1050] * channels
# max_vals = [1950] * channels

while True:
	bits = BitArray()
	line = ser.readline().strip()
	for pulse_length in line.split():
		bits.append('uint:16=' + pulse_length)
	s.sendto(bits.tobytes(), (UDP_ADDR, UDP_PORT))
	print line
