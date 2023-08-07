import time
import sys
import random
import socket
from socket import AF_INET, SOCK_DGRAM
import pickle
import fcntl
import struct

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


		def get_ip_address(ifname):
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			return socket.inet_ntoa(fcntl.ioctl(s.fileno(),0x8915,struct.pack('256s',  bytes(ifname[:15], 'utf-8')))[20:24])

		print(get_ip_address('wlo1'))  # '192.168.0.110'

		my_ip=get_ip_address('wlo1')
		my_port=int(sys.argv[1])
		address=(my_ip,my_port)
		sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
		sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		sock.bind(address)
		
		while(1):
			
			print("Waiting to receive a message from leader")
			rcvmsg=message_class()
			data = sock.recv(60000)
			print("msg len is",len(data))
			rcvmsg=pickle.loads(data)




