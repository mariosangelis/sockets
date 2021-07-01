import time
import sys
import random
import socket
from socket import AF_INET, SOCK_DGRAM
import pickle
import fcntl
import struct
import select

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
	
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		
		sock.bind(address)
		sock.listen(1024)
		
		inputs = [sock]
		outputs = []
		
		#Use select function in order to get data from multiple sockets simultaneously
		while inputs:
			readable, writable, exceptional = select.select(inputs, outputs, inputs)
			for s in readable:
				if s is sock:
					#Accept a connection. Append the file descriptor to the inputs list
					receive_connection, client_address = s.accept()
					print("Accepted a connection")
					receive_connection.setblocking(1)
					inputs.append(receive_connection)
				else:
					
					print("Received a message")
					rcvmsg=message_class()
					#Header has length equal to HEADER_LENGTH bytes
					data= s.recv(HEADER_LENGTH,socket.MSG_WAITALL)
					
					if(len(data)==0):
						print("connection has closed")
						inputs.remove(s)
						break
					
					msg_len=int(data)
					print("Wait for a message with length",msg_len)
					
					received_bytes=msg_len
					#print("Receive a message with length=",msg_len)
					#Receive the message after the header
					data=bytes()
					while(1):
						
						try:
							data+=s.recv(received_bytes)
						except BlockingIOError:
							print("receive error")
							continue
						
						if(len(data)==msg_len):
							break
						print("received bytes=",received_bytes)
						received_bytes=msg_len-len(data)
					
					rcvmsg=pickle.loads(data)

