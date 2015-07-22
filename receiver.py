# Requires bitstring module
# $ pip install bitstring

import socket
import time
from bitstring import ConstBitStream
from lib.Adafruit_PWM_Servo_Driver import PWM


udp_bind_ip = "127.0.0.1"
udp_port = 5040

pwm = PWM(0x40)
servoMin = 150
servoMax = 600
travel = servoMax - servoMin
pwm.setPWMFreq(60)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((udp_bind_ip, udp_port))

while True:
    data = s.recv(1024)
    length = len(data) * 8
    if length < 16:
        continue

    bits = ConstBitStream(bytes=data, length=length)
    while bits.pos <= length - 16:
        servo, value = bits.readlist('uint:7, int:9')
        servo_value = int((value + 255) / 512.0 * travel + servoMin)
        print "Servo:", servo, "Value:", servo_value
        pwm.setPWM(servo, 0, servo_value)

