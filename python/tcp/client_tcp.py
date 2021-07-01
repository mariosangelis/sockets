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
		HEADER_LENGTH=20
		
		server_ip="192.168.0.151"
		server_port=int(sys.argv[1])
		server_address = (server_ip,server_port)
		print(server_address)
		
		send_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		# Connect the socket to the port where the server is listening
		send_connection.connect(server_address)
		
		for i in range(0,3):
			send_message=message_class(bytearray(2000000*(i+1)))
			send_message=pickle.dumps(send_message)
			
			print("actual length=",len(send_message))
			send_message=bytes(f'{len(send_message):<20}',"utf-8") + send_message
			print("final length=",len(send_message))
			
			try:
				send_connection.sendall(send_message)
			except socket.timeout:
				#This is a timeout
				print("timeout")
				
		while(1):
			time.sleep(10)
		
