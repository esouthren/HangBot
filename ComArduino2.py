#!/usr/bin/python
import serial

import time

#The following line is for serial over GPIO
port = 'COM3' # note I'm using Mac OS-X


ard = serial.Serial(port,9600,timeout=5)
time.sleep(2) # wait for Arduino

'''
to send:
two floats

'''

i = 0
while(True):
    motor_one_val = input("Motor 1 value: ")
    if motor_one_val == "quit":
        exit()
        break
    motor_two_val = input("Motor 2 value: ")

    ard.flush()
    string_to_send = "{}>{}\n".format(str(motor_one_val), str(motor_two_val))
    print("SENT: {}".format(string_to_send))
    ard.write(string_to_send.encode())
    time.sleep(1)

    # Serial read`12 section
    msg = ard.read(ard.inWaiting()) # read all characters in buffer
    print ("\tRECEIVED: {}".format(msg))

else:
    print("Exiting")
exit()