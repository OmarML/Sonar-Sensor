import RPi.GPIO as GPIO
import time
import socket
#import matplotlib.pyplot as plt
#import matplotlib.animation as animation
#from matplotlib import style

GPIO.setmode(GPIO.BCM)

TRIG = 4
ECHO = 18 #change numbers accordingly  to pins youu have plugged into

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

IP = "192.168.1.255" # IP address of your Pi
Port = 3000 # make sure port numbers match
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

def get_distance():
        GPIO.output(TRIG, True)
        time.sleep(0.0001)
        GPIO.output(TRIG, False)

        while GPIO.input(ECHO) == False:
                start = time.time()

        while GPIO.input(ECHO) == True:
                end = time.time()

        sig_time = end - start

        #Distance in cm
        Distance = sig_time / 0.000058

        print('Distance is: {} cm'.format(Distance))
        return Distance


def Send_Distance():
        while True:
                my_message = bytes(get_distance())
                time.sleep(0.05)
                sock.sendto(my_message, (IP, Port))

Send_Distance()
        



