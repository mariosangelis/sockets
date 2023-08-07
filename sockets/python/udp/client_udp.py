import time
import sys
import random
import socket
from socket import AF_INET, SOCK_DGRAM
import pickle

class message_class:
	def __init__(self,data=None):
		self.data=data

	def get_data(self):
		return(self.data)

if __name__ == "__main__":
    
	#argv[1] is the service id and argv[2] is client's socket reply port
	if(len(sys.argv)<2):
		print("Wrong number of arguments")
	else:

		component_address = ("192.168.0.151",int(sys.argv[1]))
		print(component_address)

		send_message=message_class(bytearray(1000))
		send_message=pickle.dumps(send_message)

		sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
		#sock.settimeout(5.0)
		ackmsg=message_class();
		
		for i in range(0,3):
			try:
				sock.sendto(send_message,component_address)
			except socket.timeout:
				#This is a timeout
				print("timeout")
			
		sock.close()


