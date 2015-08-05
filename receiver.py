# Requires bitstring module
# $ sudo apt-get install python-pip
# $ sudo pip install bitstring

import socket
import time
from bitstring import ConstBitStream
from lib.Adafruit_PWM_Servo_Driver import PWM

input_min = 980
input_max = 2010

udp_bind_ip = "0.0.0.0"
udp_port = 5040

pwm = PWM(0x40)
servo_min = 150
servo_max = 600
pwm.setPWMFreq(60)

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
        servo_value = float((bits.read('uint:16') - input_min)) / input_max * servo_max + servo_min
        print "Servo:", servo, "Value:", servo_value
        pwm.setPWM(servo, 0, int(servo_value))
        servo = servo + 1
