import serial
import math
from bitstring import BitArray
import socket
import argparse

parser = argparse.ArgumentParser(description='Transmit PPM from serial.')
parser.add_argument('serial', help='the serial port to pull PPM from')
parser.add_argument('serial_rate', help='the rate in bps to connect to the serial port at', type=int)
parser.add_argument('destination_ip', help='the IP address to send PPM to')
parser.add_argument('port', help='the port to use', type=int)
args = parser.parse_args()

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ser = serial.Serial(args.serial, args.serial_rate)

while True:
	bits = BitArray()
	line = ser.readline().strip()
	for pulse_length in line.split():
		bits.append('uint:16=' + pulse_length)
	s.sendto(bits.tobytes(), (args.destination_ip, args.port))
	print line
