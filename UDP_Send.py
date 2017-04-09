import socket
import time

IP = "192.168.1.255"

Port = 3000
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

while True:
	my_message =bytes("Hello Omar!")
	sock.sendto(my_message, (IP, Port))
	print ("message sent, press CTRL+C to stop")
	time.sleep(1)
