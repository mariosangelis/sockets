#include<stdio.h>
#include<stdlib.h>
#include <pthread.h>
#include <unistd.h>
#include <semaphore.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <netinet/in.h>
#include <string.h>
#include <errno.h>
#include <netdb.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <sys/ioctl.h>
#include <netinet/in.h>
#include <net/if.h>
#include <arpa/inet.h>

char *get_my_ip();

int main(int argc,char *argv[]){
	
	int sock;
	struct sockaddr_in server;
	char message[1024],reply[1024];
	
	//Create a UDP socket
	sock = socket(AF_INET, SOCK_DGRAM, 0);
	if(sock < 0){
		fprintf(stderr,"Opening datagram socket error.Termination");
		exit(1);
	}
	
	server.sin_family = AF_INET;
	inet_aton(get_my_ip(),&server.sin_addr);
	server.sin_port = htons(10000);
	
	scanf("%s",message);
	printf("Send message: %s\n",message);
	
	//Send a discovery message to the multicast channel.
	if(sendto(sock,message,sizeof(message),0,(struct sockaddr*)&server,sizeof(server)) < 0){fprintf(stderr,"Sending message error");}
	else{printf("Sending discovery message...OK\n");}
	
	//Wait to receive a reply for the discovery message from each server which serves this specific service id
	
	recvfrom(sock,reply,1024,0,NULL,NULL);
	printf("Received reply from server: %s\n",reply);
	
	return(0);
}


char *get_my_ip(){
	
	
	int fd;
	struct ifreq ifr;
	fd = socket(AF_INET, SOCK_DGRAM, 0);

	/* I want to get an IPv4 IP address */
	ifr.ifr_addr.sa_family = AF_INET;
	strncpy(ifr.ifr_name, "wlo1", IFNAMSIZ-1);
	ioctl(fd, SIOCGIFADDR, &ifr);
	close(fd);

	return(inet_ntoa(((struct sockaddr_in *)&ifr.ifr_addr)->sin_addr));
	
}
