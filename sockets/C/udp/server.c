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
	
	int server_receiver_sock;
	struct sockaddr_in server,from;
	int fromlen=sizeof(struct sockaddr_in);
	char buffer[1024];
	
	char my_ip[100];
	
	strcpy(my_ip,get_my_ip());

	
	//Create a UDP socket
	server_receiver_sock = socket(AF_INET, SOCK_DGRAM, 0);
	if(server_receiver_sock < 0){
		fprintf(stderr,"Opening datagram socket error.\n");
		exit(1);
	}
	else{printf("Opening datagram socket....OK.\n");}
	
	server.sin_family = AF_INET;
	server.sin_port = htons(10000);

	server.sin_addr.s_addr = inet_addr(my_ip);
	if(bind(server_receiver_sock, (struct sockaddr*)&server, sizeof(server))){
		fprintf(stderr,"Binding datagram socket error.\n");
		exit(1);
	}
	else{printf("Binding datagram socket...OK.\n");}
	
	while(1){
		
		if(recvfrom(server_receiver_sock,(char *)buffer,1024,0,(struct sockaddr *)&from,(socklen_t *)&fromlen)<=0){printf("An error has occured in recvfrom\n");}
		
		printf("Received message: %s\n",buffer);
		sendto(server_receiver_sock,"ack",sizeof("ack"),0,(struct sockaddr*)&from,sizeof(from));
		
	}
	
	
	
	
	
	
	
	
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
