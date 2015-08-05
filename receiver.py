# Requires bitstring module
# $ pip install bitstring

import socket
import time
from bitstring import ConstBitStream
import argparse
# from lib.Adafruit_PWM_channel_Driver import PWM

parser = argparse.ArgumentParser(description='Receive PPM in UDP packets and map to local PWM.')
parser.add_argument('port', help='the port to use', type=int)
args = parser.parse_args()

# pwm = PWM(0x40)
# pwm.setPWMFreq(60)

pwm_min = 400
pwm_max = 650

input_mins = []
input_maxs = []

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('0.0.0.0', args.port))

while True:
    data = s.recv(1024)
    length = len(data) * 8
    if length < 16 or length % 16 != 0:
        continue

    bits = ConstBitStream(bytes=data, length=length)
    channel = 0
    while bits.pos <= length - 16:
        channel_value = bits.read('uint:16')

        # Set new min/max for channel if necessary
        if len(input_mins) <= channel:
            input_mins.append(channel_value)
            input_maxs.append(channel_value)
        if channel_value < input_mins[channel]:
            input_mins[channel] = channel_value
        elif channel_value > input_maxs[channel]:
            input_maxs[channel] = channel_value
        if input_mins[channel] == input_maxs[channel]:
            continue

        # Map channel value to pwm value
        pwm_value = float(channel_value - input_mins[channel]) * (pwm_max - pwm_min) / (input_mins[channel] - input_maxs[channel]) + pwm_min;

        print "Channel:", channel, "Input:", channel_value, "PWM:", pwm_value
        # pwm.setPWM(channel, 0, pwm_value)
        channel = channel + 1
