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
	
		print(get_ip_address('wlo1'))  # '192.168.0.110'
	
		my_ip=get_ip_address('wlo1')
		my_port=int(sys.argv[1])
		address=(my_ip,my_port)
	
	
	
	
		sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
		sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		sock.bind(address)
	
	
		time.sleep(10000)
	
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		
		
		sock.bind(address)
		sock.listen(1024)
		
		#conn, addr = sock.accept()
		inputs = [sock]
		outputs = []
		
		
		time.sleep(5)
		print("6666666666666666666666666666666666666666666666666666666666666666")
		
		#Use select function in order to get data from multiple sockets simultaneously
		while inputs:
			print("rrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr")
			readable, writable, exceptional = select.select(inputs, outputs, inputs)
			for s in readable:
				if s is sock:
					print("7777777777777777777777777777777777777777777777777777777777777777777777")
					#Accept a connection. Append the file descriptor to the inputs list
					receive_connection, client_address = s.accept()
					print("Accepted a connection")
					receive_connection.setblocking(1)
					inputs.append(receive_connection)
				else:
					
					print("Waiting to receive a message from leader")
					rcvmsg=message_class(0,0,0,0)
					#Header has length equal to 20 bytes
					data= s.recv(20,socket.MSG_WAITALL)

					if(len(data)==0):
						print("connection has closed")
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
					
					
					
				
					#data= s.recv(msg_len)
					rcvmsg=pickle.loads(data)

					if(rcvmsg.get_type()==12000):
						print("Got a message from leader. Send my data to ip",rcvmsg.get_ip(),"and port",rcvmsg.get_port())
						
						
					
