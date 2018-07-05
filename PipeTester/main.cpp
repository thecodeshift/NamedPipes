#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <thread>
#include <string.h>

#include <sys/stat.h>
#include <unistd.h>
#include <fcntl.h>

#define PIPE_RESPONSE "pipe_response"
#define PIPE_REQUEST "pipe_request"

void initPipes() 
{
	int response = mkfifo("pipe_response", 0666);

	int request = mkfifo("pipe_request", 0666);
}

void client()
{
	int fdResponse = open("pipe_response", O_RDONLY);
	std::cout << "[CLIENT] Response pipe opened: " << fdResponse << std::endl;

	int fdRequest = open("pipe_request", O_WRONLY);
	std::cout << "[CLIENT] Request pipe opened: " << fdRequest << std::endl;

	char buffer[1024];

	while (true)
	{
		buffer[0] = 1;
		buffer[1] = 2;

		if (write(fdRequest, buffer, 2) == -1)
			break;

		int result = read(fdResponse, buffer, 1);

		if (result != 1)
		{
			std::cout << "[CLIENT] Read result: " << result << std::endl;

			break;
		}

		int len = buffer[0];
		result = read(fdResponse, buffer, len);

		if (result != len)
		{
			std::cout << "[CLIENT] Read result: " << result << std::endl;

			break;
		}

		buffer[len] = '\0';

		std::cout << "[CLIENT] Server response: " << buffer << std::endl;

		std::this_thread::sleep_for(std::chrono::seconds(1));
	}
}

void server()
{
	initPipes();

	int fdResponse = open("pipe_response", O_WRONLY);
	std::cout << "[SERVER] Response pipe opened: " << fdResponse << std::endl;

	int fdRequest = open("pipe_request", O_RDONLY);
	std::cout << "[SERVER] Request pipe opened: " << fdRequest << std::endl;

	char buffer[1024];
	char aux[128];
	int count = 0;

	while (true)
	{
		int result = read(fdRequest, buffer, 1024);

		if (result != 2)
		{
			std::cout << "[SERVER] Read result: " << result << std::endl;

			break;
		}

		sprintf(aux, "%d", ++count);

		int len = strlen(aux);

		buffer[0] = len;

		strcpy(buffer + 1, aux);

		std::cout << "[SERVER] Payload write: " << aux << std::endl;

		result = write(fdResponse, buffer, len + 1);

		if (result == -1)
		{
			std::cout << "[SERVER] Response result: " << result << std::endl;

			break;
		}
	}
}

int main(int argc, char* argv[])
{
	if (*(argv[1]) == 's')
	{
		server();
	}
	else
	{
		client();
	}
}