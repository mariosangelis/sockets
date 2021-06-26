import time
import sys
import random
import socket
from socket import AF_INET, SOCK_DGRAM
import pickle

class message_class:
	def __init__(self,msg_type,data,dst_ip,dst_port):
		self.msg_type=msg_type
		self.data=data
		self.dst_ip=dst_ip
		self.dst_port=dst_port

	def get_data(self):
		return(self.data)

	def get_type(self):
		return(self.msg_type)

	def get_ip(self):
		return(self.dst_ip)

	def get_port(self):
		return(self.dst_port)


if __name__ == "__main__":
    
	#argv[1] is the service id and argv[2] is client's socket reply port
	if(len(sys.argv)<2):
		print("Wrong number of arguments")
	else:

		component_address = ("192.168.0.137",9400)
		print(component_address)

		send_message=message_class(12000,bytearray(1000),"192.168.1.100",9700)
		send_message=pickle.dumps(send_message)

		sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
		#sock.settimeout(5.0)
		ackmsg=message_class(0,0,0,0);
		
		for i in range(0,3):
			try:
				sock.sendto(send_message,component_address)
			except socket.timeout:
				#This is a timeout
				print("timeout")
			
		sock.close()


