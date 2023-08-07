#include <stdio.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <stdlib.h>
#include <arpa/inet.h>
#include <string.h>
#include <pthread.h>
#include <unistd.h>

struct thread_info{
	pthread_t thread_id;
	int connection_fd;
	
};

void *my_receiver(void *arg);
int main(int argc,char *argv[]){
	
	int sock,len,i=0,iret;
	struct sockaddr_in serveraddr,client_addr;
	
	struct thread_info info[10];
	
	sock = socket(AF_INET,SOCK_STREAM,0);
	if(sock == -1){
		printf("Server socket creation failed\n");
		exit(1);
	}
	
	serveraddr.sin_family = AF_INET;
	inet_aton("192.168.1.123", &(serveraddr.sin_addr));
	
	serveraddr.sin_port = htons(atoi(argv[1]));
	
	if(bind(sock,(struct sockaddr *)&serveraddr,sizeof(serveraddr))!=0){
		printf("Server socket bind failed\n");
		exit(1);
	}
	
	printf("address is %s and port is %d\n",inet_ntoa(serveraddr.sin_addr),ntohs(serveraddr.sin_port));
	
	if(listen(sock,5)<0){
		printf("Server socket listen failed\n");
		exit(1);
	}
	
	len=sizeof(struct sockaddr_in);
	
	
	
	while(1){
		info[i].connection_fd = accept(sock,(struct sockaddr*)&client_addr,(socklen_t *)&len);
	
		if(info[i].connection_fd<0){
			printf("Server socket accept failed\n");
			exit(1);
		}
		
		printf("Server accepted a client with ip=%s and port=%d\n",inet_ntoa(client_addr.sin_addr),ntohs(client_addr_temp.sin_port));
		
		iret = pthread_create(&(info[i].thread_id),NULL,my_receiver,(void *)(&info[i]));
		if(iret){
			fprintf(stderr,"Error - pthread_create() return code: %d\n",iret);
			exit(EXIT_FAILURE);
		}
		i++;
		
	}
	
	
	return(0);
}

void *my_receiver(void *arg){
	
	struct thread_info *thread_struct=(struct thread_info*)arg;
	char *message = (char*)malloc(100);
	printf("Hello from thread with id = %ld\n",thread_struct->thread_id);
	
	while(1){
		recv(thread_struct->connection_fd,message,100,0);
		printf("Thread %ld got a message which is %s\n",thread_struct->thread_id,message);
		send(thread_struct->connection_fd,"ACK",3,0);
		memset(message,0,100);
	}

	
}

