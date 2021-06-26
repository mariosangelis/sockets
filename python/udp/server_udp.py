import time
import sys
import random
import socket
from socket import AF_INET, SOCK_DGRAM
import pickle
import fcntl
import struct

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


		def get_ip_address(ifname):
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			return socket.inet_ntoa(fcntl.ioctl(s.fileno(),0x8915,struct.pack('256s',  bytes(ifname[:15], 'utf-8')))[20:24])

		print(get_ip_address('eth0'))  # '192.168.0.110'

		my_ip=get_ip_address('eth0')
		my_port=int(sys.argv[1])
		address=(my_ip,my_port)
		sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
		sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		sock.bind(address)
		

		time.sleep(10)
		while(1):
			
			print("Waiting to receive a message from leader")
			rcvmsg=message_class(0,0,0,0)
			data = sock.recv(60000)
			print("msg len is",len(data))
			rcvmsg=pickle.loads(data)

			if(rcvmsg.get_type()==12000):
				print("Got a message from leader. Send my data to ip",rcvmsg.get_ip(),"and port",rcvmsg.get_port())





