# Requires bitstring module
# $ pip install bitstring

import socket
import time
from bitstring import ConstBitStream
from lib.Adafruit_PWM_Servo_Driver import PWM


udp_bind_ip = "0.0.0.0"
udp_port = 5040

pwm = PWM(0x40)
pwm.setPWMFreq(1000)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((udp_bind_ip, udp_port))

while True:
    data = s.recv(1024)
    length = len(data) * 8
    if length < 16 or length % 16 != 0:
        continue

    bits = ConstBitStream(bytes=data, length=length)
    servo = 0
    while bits.pos <= length - 16:
        servo_value = bits.read('int:16')
        print "Servo:", servo, "Value:", servo_value
        pwm.setPWM(servo, 0, servo_value)
        servo = servo + 1