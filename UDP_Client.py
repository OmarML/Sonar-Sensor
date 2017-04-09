import socket
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

UDP_IP = "192.168.1.33"
UDP_PORT = 3000

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
sock.bind((UDP_IP, UDP_PORT))

xs = []
ys = []
start = time.time()
while True:
    data, addr = sock.recvfrom(1024)   # buffer size is 1024 bytes
   print("received message: {}".format(data))
#    xs.append((time.time() - start))
#    ys.append(data)
#    plt.plot(xs, ys)
#    plt.xlabel("Time (s)")
#    plt.ylabel("Altitude (cm)")
#    plt.show()