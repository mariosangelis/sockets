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
		component_address = ("192.168.1.7",9000)
		print(component_address)
		
		send_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		# Connect the socket to the port where the server is listening
		send_connection.connect(component_address)

		for i in range(0,3):
			send_message=message_class(12000,bytearray(2000000*(i+1)),"192.168.1.100",9700)
			send_message=pickle.dumps(send_message)
			
			print(len(send_message))
			send_message=bytes(f'{len(send_message):<20}',"utf-8") + send_message
			print("final length=",len(send_message))

			try:
				send_connection.sendall(send_message)
			except socket.timeout:
				#This is a timeout
				print("timeout")
				
		while(1):
			time.sleep(10)
