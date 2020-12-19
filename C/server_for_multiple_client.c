#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <netdb.h>
void error(const char *msg)
{
    perror(msg);
    exit(1);
}
int main(int argc, char *argv[])
{
     int sockfd, newsockfd, portno;
     socklen_t clilen;
     pid_t childpid;
     char buff[256],ans[10];
     struct sockaddr_in serv_addr, cli_addr;
     int n;
     if (argc < 2) {
         fprintf(stderr,"ERROR, no port provided\n");
         exit(1);
     }
     sockfd=socket(AF_INET, SOCK_STREAM, 0);
     if (sockfd < 0) 
        error("ERROR opening socket");
     bzero((char *) &serv_addr, sizeof(serv_addr));
     portno = atoi(argv[1]);
     serv_addr.sin_family = AF_INET;
     serv_addr.sin_addr.s_addr = INADDR_ANY;
     serv_addr.sin_port = htons(portno);
     if (bind(sockfd, (struct sockaddr *) &serv_addr,sizeof(serv_addr)) < 0)
              error("ERROR on binding");
     listen(sockfd,5);
     clilen = sizeof(cli_addr);

     	while(1)
        {
	     
         newsockfd = accept(sockfd, (struct sockaddr *) &cli_addr,&clilen);
		if(newsockfd < 0){
			exit(1);
		}
		printf("Connected with client socket number %d\n",newsockfd);

		if((childpid = fork()) == 0){
			close(sockfd);
     
     while(1)
     {
        bzero(buff,256);
        n=read(newsockfd,buff,255);
        if (n < 0) error("ERROR reading from socket");
        printf("\nClient socket number %d sent message: %s\n",newsockfd,buff);
        if(strncmp("Bye", buff, 3)==0)
        {
            strcpy(ans,"Goodbye");
            printf("Replied to client %d\n",newsockfd);
            printf("Client said bye; finishing\n");
            n = write(newsockfd,ans,strlen(ans));
            if (n < 0) error("ERROR writing to socket");
            close(newsockfd);
            break;
        }
        strcpy(ans,"OK");
        n = write(newsockfd,ans,strlen(ans));
        if (n < 0) error("ERROR writing to socket");
        printf("Replied to client %d\n",newsockfd);
     }
    }
}
     return 0; 
}