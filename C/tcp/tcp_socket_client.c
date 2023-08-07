#include <stdio.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <stdlib.h>
#include <arpa/inet.h>
#include <string.h>

int main(int argc,char *argv[]){
	int sock;
	
	struct sockaddr_in serveraddr;
	char *message = (char *)malloc(100);
	
	sock = socket(AF_INET,SOCK_STREAM,0);
	if(sock == -1){
		printf("Server socket creation failed\n");
		exit(1);
	}
	
	serveraddr.sin_family = AF_INET;
	inet_aton("192.168.1.123", &(serveraddr.sin_addr));
	serveraddr.sin_port = htons(atoi(argv[1]));
	
	if(connect(sock,(struct sockaddr *)&serveraddr, sizeof(serveraddr)) != 0){ 
		printf("Connection with the server failed \n"); 
		exit(1);
	}
	
	
	
	while(1){
		memset(message,0,100);

		printf("Give a message: ");
		scanf("%s",message);
		send(sock,message,100,0);
		
		memset(message,0,100);
		recv(sock,message,100,0);
		printf("Returned message is %s\n",message);
		
	}
	
	return(0);
}
